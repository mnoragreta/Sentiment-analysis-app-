Sentiment Analysis API with Flask & Docker

Project Overview

This project is a Sentiment Analysis API built using Flask, Random Forest, and TF-IDF vectorization. It is containerized with Docker and uses MySQL as the database backend. The API receives text input, processes it using a pre-trained Random Forest model, and returns a sentiment score.

Project Structure

├── app/                 # Contains the Flask application
│   ├── app.py           # Main Flask app handling requests
│   ├── Dockerfile       # Dockerfile for API container
│   ├── index.html       # Frontend interface for testing API
│   ├── vectorization.pkl # TF-IDF vectorizer
│   ├── randomforest.pkl # Trained Random Forest model
│   ├── requirements.txt # Dependencies for Flask app
│
├── dataset/             # (Optional) Raw dataset used for training
│
├── db/                  # Contains MySQL database setup
│   ├── init.sql         # SQL file for database initialization
│
├── docker-compose.yml   # Docker Compose configuration file


How It Works

Model Training (Preprocessing Stage)

A Jupyter Notebook was used to preprocess a dataset.

The dataset was vectorized using TF-IDF.

A Random Forest classifier was trained on the transformed dataset.

The trained vectorizer and model were saved as .pkl files.


Flask API

The Flask app loads the TF-IDF vectorizer and Random Forest model.

It exposes an endpoint (/predict) where users can send text data.

The model predicts whether the sentiment is positive or negative.


Database (MySQL)

A MySQL database stores processed sentiment results.

The init.sql file sets up the database schema.


Docker Containerization

The project is containerized using Docker.

The docker-compose.yml file sets up two services:

mysql_db: MySQL database container.

sentimentflaskapp: Flask API container.

These services communicate internally.


Installation & Setup

Prerequisites

Docker & Docker Compose installed on your system




Future Improvements

Deploy on AWS/GCP/Azure

Improve model performance with fine-tuning

Add more ML models for comparison

Create a frontend dashboard