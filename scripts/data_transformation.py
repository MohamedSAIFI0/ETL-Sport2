import pandas as pd


#----------------------Load the Dataset----------------------#
df = pd.read_json(r"C:\Users\P15\Desktop\ETL\data\data.json")

#--------------------- Understand the Data-------------------#
#check basic info
print(df.info())

#Summary statistics
print(df.describe())

#Check for missing values
print(df.isnull().sum())

#check column names
print(df.columns)

#check data types
print(df.dtypes)


#---------------------- Data Cleaning -------------------------#

#Fill missing values in a specific column with the mean
df["Goals"].fillna(df["Goals"].mean(),inplace=True)
df["Assists"].fillna(df['Assists'].mean(),inplace=True)
df["Points"].fillna(df["Points"].mean(), inplace=True)

#Drop rows with missing values
df.dropna(inplace=True)

#Check for duplicates and drop them
print(df.duplicated().sum())
df.drop_duplicates(inplace=True)

#Covert to numeric
df["Matches Won"] = pd.to_numeric(df["Matches Won"])


#-----------------------Feature Engineering (Data Transformation)-----------#

df["total_goals"] = df["Games Played"] * df["Goals"]

grouped_df = df.groupby("Sport").agg({
    "Games Played":"sum",
    "Goals":"sum",
    "Assists":"sum"
}).reset_index()

filterd_df = grouped_df.sort_values("Goals",ascending=True)

df.to_csv(r"C:\Users\P15\Desktop\ETL\data\transformed_data.csv",index=False)
filterd_df.to_csv(r"C:\Users\P15\Desktop\ETL\data\filtered_data.csv",index=False)
