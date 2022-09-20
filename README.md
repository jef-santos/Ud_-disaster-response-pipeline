# Disaster Response Pipeline Project

## 1. Project Overview
This project is part of the Udacity Data Science Nanodegree. The challenge at hand was to create a way to classify messages received online about natural disasters. For this, it was used a database made available by Figure Eight with dozens of messages that they dealt with over the years.

In this way, the project creates a web app that, from a machine learning model, classifies new messages.

## 2. Project Components
### Data
In the "data" repository we have the raw bases: data/disaster_messages.csv and data/disaster_categories.csv.
They pass through the ETL pipeline through the data/process_data.py file, thus generating a treated base called data/DisasterResponse.db

## 3. Running

1. Run the following commands in the project's root directory to set up the database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Go to `app` directory: `cd app`

3. Run your web app: `python run.py`

4. Go to http://0.0.0.0:3001/

## 4. Conclusion
