# Disaster Response Pipeline Project

## Table of Contents
1. Project Overview
2. Project Components
3. Running

## 1. Project Overview
This project is part of the Udacity Data Science Nanodegree. The challenge at hand was to create a way to classify messages received online about natural disasters. For this, it was used a database made available by Figure Eight with dozens of messages that they dealt with over the years.

In this way, the project creates a web app that, from a machine learning model, classifies new messages.

This application is important and relevant to help classify and target messages when major disasters happen. Once we managed to finish the message content a specific team to answer. For example messages from people requesting water will be answered by the most suitable team.

## 2. Project Components

<pre>
├── app
│   ├── run.py------------------------# Flask file that runs app
│   └── templates
│       ├── go.html-------------------# classification result page of web app
│       └── master.html---------------# main page of web app
├── data
│   ├── DisasterResponse.db-----------# database to save clean data to
│   ├── disaster_categories.csv-------# data to process
│   ├── disaster_messages.csv---------# data to process
│   └── process_data.py---------------# perfoms ETL process
├── files-----------------------------# images from web app
├── models
│   ├── classifier.pkl----------------# saved model
│   └── train_classifier.py-----------# performs classificaton Task
└── README.md
</pre>

### Data
In the "data" repository we have the raw bases: disaster_messages.csv and disaster_categories.csv.
They pass through the ETL pipeline through the process_data.py file, thus generating a treated base called DisasterResponse.db
- Loads the messages and categories dataset
- Merges the two datasets
- Cleans the data
- Stores it in a SQLite database

### Model
In the model repository we have the train_classifier.py pipeline responsible for creating the machine learning model entitled classifier.pkl.
- Loads data from the SQLite database
- Splits the data into training and testing sets
- Builds a text processing and machine learning pipeline
- Trains and tunes a model using GridSearchCV
- Outputs result on the test set
- Exports the final model as a pickle file

## 3. Running

1. Run the following commands in the project's root directory to set up the database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Go to `app` directory: `cd app`

3. Run your web app: `python run.py`

4. Go to http://0.0.0.0:3001/





