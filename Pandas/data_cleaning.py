import pandas as pd

df = pd.read_csv("Pandas\data.csv")

############ Printing first dimension of data ######
print("The original dimension of the dataset without cleaning: ", df.shape)

############# Fixed date format ####################
df['Date'] = pd.to_datetime(df['Date'], format = 'mixed')

############# Dropped Null value in Date ###########
df.dropna(subset = ['Date'], inplace=True)

############# Changing a data ######################
for x in df.index:
    if df.loc[7,'Duration'] > 120:
        df.loc[7, 'Duration'] = 120

############# Dropping duplicates ##################
df.drop_duplicates(inplace=True)

############# Printing final result ################
print(df.to_string())
print("The final dimension of the dataset: " , df.shape)