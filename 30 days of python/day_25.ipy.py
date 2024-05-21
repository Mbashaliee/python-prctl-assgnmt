#getting the first five rows
import pandas as pd
import numpy as np
data=[
    ['Asabenah', 'finland', 'Helsinki'],
    ['David', 'UK', 'London'],
    ['John', 'Sweden', 'Stockholm'],
    ['Musa', 'Niger', 'Yamen'],
    ['ALiyu', 'UAE', 'Dubai'],
]
df = pd.DataFrame(data, columns=['Names', 'Country', 'City'])
df.head(5)

print(df)

#getting the last five rows
df.tail(5)
print(df.tail(5))


#gettting the title column as pandas series
df=pd.DataFrame({'title': ['movie1', 'movie2', 'movie3', 'movie4']})

title_series=df['title']
print(title_series)

#filtering out the titles with python
df.shape
df=pd.DataFrame({'title': ['python for beginners', 'java programming', 'python data sceince', 'C++ Basics', 'python machine learning']})
python_titles=df[df['title'].str.contains('python')]
print(python_titles)


#filtering out the titles with python
javascript=df[df['title'].str.contains('javascript')]
print(javascript)

df.shape

print(df.shape)

print(df['title'].value_counts())
