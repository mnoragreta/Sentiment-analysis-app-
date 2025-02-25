from flask import Flask, request, jsonify, send_from_directory
import pickle
import time
from datetime import datetime
import pymysql

# Initialize Flask app
app = Flask(__name__)

# Load the pickled model and vectorizer at the start of the application
with open('app/randomforest_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('app/vectorization.pkl', 'rb') as vec_file:
    vectorizer = pickle.load(vec_file)

print('vectorization is unpickeled')

DB_HOST = "db"
DB_USER = "root"
DB_PASSWORD = "root"
DB_NAME = "Model_Logger"
#DB_PORT=3306

def log_to_db(input_params, output, response_time):
    try:
        print("Connecting to DB")
        connection = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
            #port=3306
        )
        print("Entering log_to_db")

        with connection.cursor() as cursor:
            sql = """
            INSERT INTO Log (Current_Date_Time, Input_Params, Output, Response_Time)
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(sql, (datetime.now(), str(input_params), str(output), response_time))

        connection.commit()
        print("Data Inserted")

    except Exception as e:
        # Log any database connection or query error
        print(f"Error logging to DB: {e}")
    
    finally:
        # Ensure the connection is closed even if an error occurs
        if 'connection' in locals() and connection.open:
            connection.close()
            print("Database connection closed.")


@app.route('/')
def home():
    return send_from_directory('.', 'index.html')  # Serve index.html from the current directory


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the sentiments text from the request JSON
        data = request.get_json(force=True)
        sentiment_text = data.get('sentiments')
        print(sentiment_text)
        if not sentiment_text:
            return jsonify({'error': 'No sentiment text provided'}), 400

        # Start the timer
        start_time = time.time()

        # Vectorize the input sentiment text
        sentiment_vector = vectorizer.transform([sentiment_text])

        # Perform prediction
        prediction = model.predict(sentiment_vector)

        # Map prediction to human-readable response
        result = 'Negative sentiment' if prediction[0] == 1 else 'Positive sentiment'

        # if prediction[0] == 1:
        #     result = "Positive sentiment"
        # else:
        #     result = "Negative sentiment"

        # Return the result as JSON
        response_time = time.time() - start_time
    

        try:
            log_to_db(input_params=data, output=result, response_time=response_time)
        except Exception as e:
            print(f"Logging error: {e}")
        # Return the result as JSON
        return jsonify({'prediction': result}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=50000, debug=True)