# Data Cleaning for Netflix Data

### Description: 
Wrote a python script to clean, transform and give back a CSV data to powerBI app to perform analysis on clean data. 

Initial round of cleaning just had removing empty, duplicates, trimming all the column values. After trying to analyse using powerBI, we realized our country column is not transformed cleanly.
We found that the country column in the csv had list of countries and if we try to analyze based on the country, the results weren't accurate. 

For example: If one show had country as 'United States' and the other show_id had "United States, India", now if we search for just "United States" content we got only the first show_Id as response. 

Instead of trying to make any changes in the powerBI query, tried to explore more on python, pandas, pandasql and csv library and tried to make the analysis work easy by giving two CSV files. One of them with cleaned data and new columns added and the other one with Country to show_id mapped to each other for all unique countries. Adding the relationship between the two dbs, helped us improve this situation better.
When we searched for "Argentina" we found we had 35 Contents. But with this improvement we found that originally 65 contents were released in Argentina.

This is what we have as part of the second Iteration we did on this cleaning. This could further be improved. 

Files attached: 
1. netflix_titles.csv : Raw data from Kaggle
2. netflix_titles_cleaned.csv: Cleaned data using our script
3. CountryToShowidMapper.csv: Mapper to solve the country issue discussed above
