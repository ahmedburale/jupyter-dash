import pandas as pd

s = pd.Series([42, 21, 7, 3.5])
print(s)



# Create a DataFrame
df = pd.DataFrame({'age':[18,25,39],'name':['Ahmed', 'Aisha','Mary'], 'Occupation':['Student', 'Instructor','Principal']})
print(df)

#Select by Column
print(df['age'])

#Select by Index and Slice
print(df[2:3])
print(df.iloc[2,1])

#boolean indexing
print(df[df['age']>30])

#Select by Label
print(df.loc[:, 'name'])

print(df.loc[:, ['age', 'Occupation']])

# Modifiying an Existing Dataframe
df['age'] = 19
print(df)

df.loc[1:,'age'] = 16
print(df)