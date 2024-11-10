import pandas as pd
import numpy as np

#Load data function
def load_data(df):
    data=pd.read_csv(df)
    return data

def print_top(df):
    print('Top 5 records')
    print(df.head())

def data_summary(df):
    print('Summary of the data')
    print (df.describe())

def identify_unique(df):
    print('Unique Values')
    for column in df.select_dtypes(include='object').columns:
        print(f'{column} : {df[column].unique()}')

def identify_null(df):
    print('Are there any null values?')
    print(df.isnull())
    print('Total Null records')
    print (df.isnull().sum())

def handle_missing_data(df,strategy,fill_value):
    if strategy == 'fill':
        df=df.fillna(fill_value)
    elif strategy == 'drop':
        df=df.dropna()
    elif strategy == 'flag':
        df['missing_flag']=df.isnull().any(axis=1)
    return df

def filter_column(df,col,value):
    filtered_df = df[df[col]==value]
    print (filtered_df)

#def filter_range(df,col,min,max):

#load data
df=load_data('/Users/adityakadam/Study/Python/AI/ML Course/Assignment2/ecommerce_sales_data.csv')

#Print top 5 rows
print_top(df)

#Display descriptive statistics for numerical columns
data_summary(df)

identify_unique(df)

identify_null(df)

print(handle_missing_data(df,strategy='flag',fill_value=0))

filter_column(df,'Product','Monitor')

#filter_range(df,col,min,max)

