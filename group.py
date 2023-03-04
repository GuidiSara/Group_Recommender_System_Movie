import pandas as pd
from sorted_members import *

class Group:
    def __init__(self):
        self.data = pd.read_csv(r'C:\Users\guidi\Desktop\università\progettoSII_vs\dataset\data.csv', sep=';', names=['user_id', 'movie_id', 'rating', 'timestamp'])
        self.users = pd.read_csv(r'C:\Users\guidi\Desktop\università\progettoSII_vs\dataset\users.csv', sep=';', names=['user_id', 'age', 'gender', 'occupation', 'zip_code'])
        self.items = pd.read_csv(r'C:\Users\guidi\Desktop\università\progettoSII_vs\dataset\items.csv', sep=';', names=['movie_id', 'movie_title', 'release_date', 'video_release_date', 'IMDb_url', 'unknown', 'action', 'adventure', 'animation', 'childeren', 'comedy', 'crime', 'documentary', 'drama', 'fantasy', 'film_noir', 'horror', 'musical', 'mystery', 'romance', 'sci_fi', 'thriller','war','western'])
        self.members= sortedMembers(len(self.users))
        self.data_training = pd.read_csv(r'C:\Users\guidi\Desktop\università\progettoSII_vs\dataset\training.csv', sep=';', names=['user_id', 'movie_id', 'rating', 'timestamp'])
        self.data_test = pd.read_csv(r'C:\Users\guidi\Desktop\università\progettoSII_vs\dataset\test.csv', sep=';', names=['user_id', 'movie_id', 'rating', 'timestamp'])


    
    def deleteColun(self):
        self.items.drop(['video_release_date'], axis=1, inplace=True)
        self.items.drop(['IMDb_url'], axis=1, inplace=True)
        self.items.drop(['release_date'], axis=1, inplace=True)
        self.data.drop(['timestamp'], axis=1, inplace=True)
        self.data_training.drop(['timestamp'], axis=1, inplace=True)
        self.data_test.drop(['timestamp'], axis=1, inplace=True)
        self.users.drop(['occupation'], axis=1, inplace=True)
        self.users.drop(['zip_code'], axis=1, inplace=True)
        return self

        


    