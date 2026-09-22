import pandas as pd
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(url)
print(df.shape)
print(df.head())
print(df.columns.tolist())
print(df.shape)
print(df.isnull().sum())
df = df.drop(columns=['Cabin'])
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Embarked'] = df['Embarked'].fillna({'Embarked': df['Embarked'].value_counts().index[0]})
print(df.groupby('Survived')['Survived'].count())
print(df)
