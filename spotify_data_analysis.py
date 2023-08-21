# -*- coding: utf-8 -*-
"""Spotify_Data_Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AcUdmNaNb3FhN2OUAuElO2rcDu--EZ1f

# Data and ETL Process
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df_tracks= pd.read_csv('Spotify.csv')
df_tracks

#find Null values
pd.isnull(df_tracks).sum()

df_tracks['duration_ms'] = (df_tracks['duration_ms'] / 1000)
df_tracks.rename({'duration_ms': 'duration_sec'}, axis=1, inplace=True)
df_tracks.head()

#Remove all the spaces
df_tracks['artist_name'] = df_tracks['artist_name'].str.replace(" ", "")
df_tracks

"""# Data Analysis

**1. Every genre will have all unique song two genre will not have one song**
"""

sorted_df = df_tracks.sort_values('popularity', ascending = False)
df_onetracks=sorted_df.drop_duplicates(subset='track_name',keep='first')
df_onetracks

"""2. sorting down according to the basis of the genre"""

df = df_onetracks.groupby(['genre', 'artist_name'])
df.first()

"""3. find the songs of the artist"""

df= df_onetracks.groupby('artist_name')
df.get_group(input('Enter the artist name'))

"""4. Descriptive Statistics"""

df_onetracks.describe().transpose()

"""5. most of the songs in which Genre"""

df_numbercharteds=df_tracks.groupby('genre').count().sort_values('track_name', ascending=False)
df_numbercharteds=df_numbercharteds.reset_index()
df_numbercharteds

"""6. Most songs in which genre"""

plt.figure(figsize=(25,5))
plt.title("Duration of the Songs in Different Genres")
sns.color_palette("rocket", as_cmap= True)
sns.barplot(x='genre', y='duration_sec', data=df_numbercharteds)
plt.ylabel("Duration in seconds")
plt.xlabel("Genres")

"""7. to determine who has most duration"""

df_numberchart=df_onetracks.groupby('artist_name').sum().sort_values('duration_sec', ascending=False)
df_numberchart=df_numberchart.reset_index()
df_numberchart

"""8. to determine who has most duration"""

sns.set_style(style = "darkgrid")
plt.figure(figsize=(20,5))
famous= df_numberchart.sort_values('duration_sec', ascending = False).head(10)
sns.barplot(x='artist_name', y='duration_sec', data = famous).set(title= "artist by durations")
plt.ylabel("Duration")

"""9. How many songs each artists have"""

df_numbercharted=df_onetracks.groupby('artist_name').count().sort_values('track_name', ascending=False)
df_numbercharted=df_numbercharted.reset_index()
df_numbercharted

"""10. The Most Popular Artist"""

df_numberchartedss=df_onetracks.groupby('artist_name').mean().sort_values('popularity', ascending=False)
df_numberchartedss=df_numberchartedss.reset_index()
df_numberchartedss

artist = df_onetracks['artist_name'].unique()
len(artist)

"""11. Which genre has more popularity"""

df_number=df_tracks.groupby('genre').mean().sort_values('popularity', ascending=False)
df_number=df_number.reset_index()
df_number

sns.set_style(style = "darkgrid")
plt.figure(figsize=(25,5))
famous= df_number.sort_values("popularity", ascending = False)
sns.barplot(x='genre', y='popularity', data = famous).set(title= "Genres by Popularity")

sns.set_style(style = "darkgrid")
plt.figure(figsize=(20,5))
famous= df_numberchartedss.sort_values('popularity', ascending = False).head(10)
sns.barplot(x='artist_name', y='popularity', data = famous).set(title= "artist by Popularity")
plt.ylabel("Popularity")

import seaborn as sn
sn.set(rc = {'figure.figsize':(12,10)})
sn.heatmap(df_onetracks.corr(), annot=True)
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns
df_onetrackss = df_onetracks.head(100)
plt.figure(figsize=(15,10))
sns.regplot(data=df_onetrackss, y='energy', x='speechiness', color='c').set(title=' Energy vs Speechiness Correlation')

plt.figure(figsize=(18,6))
sns.regplot(data = df_onetracks, y= "loudness", x = "energy", color = "C").set(title="Loudness vs Energy Correlation")