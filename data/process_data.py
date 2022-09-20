'''
Process Data
Project: Disaster Response Pipeline (Udacity - Data Science Nanodegree)

Arguments:
    1) Path to the CSV file containing messages
    2) Path to the CSV file containing categories
    3) Path to SQLite destination database
'''

# imports
import sys
import pandas as pd
from sqlalchemy import create_engine

def load_data(messages_filepath, categories_filepath):
    '''
    Return a dataframe with data from messages and categories merged
    input: messages and categories path
    output: a dataframe merged named df
    '''

    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)
    
    df = messages.merge(categories, on='id')
    
    return df

def clean_data(df):
    '''
    Clean the dataframe preparing it for use by the ML model
    input: df
    output: cleaned df
    '''

    #split categories
    categories = df['categories'].str.split(pat=';',expand=True)
    
    #fix categories columns names
    row = categories.iloc[0,:].values
    new_cols = [r[:-2] for r in row]
    categories.columns = new_cols

    #convert category values to 0 or 1
    for column in categories:
        categories[column] = categories[column].str[-1]
        categories[column] = pd.to_numeric(categories[column])
    
    #replaces the category column with the clean category columns
    df.drop('categories', axis = 1, inplace = True)
    df[categories.columns] = categories
    df.drop_duplicates(inplace = True)

    return df

def save_data(df, database_filename):
    '''
    Save the dataframe into a SQL database
    input: df, database_file_name str
    output: SQL database
    '''
    
    engine = create_engine('sqlite:///{}'.format(database_filename)) 
    db_filename = database_filename.split("/")[-1]
    table_name = db_filename.split(".")[0]
    df.to_sql(table_name, engine, index=False, if_exists = 'replace')


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


# run
if __name__ == '__main__':
    main()