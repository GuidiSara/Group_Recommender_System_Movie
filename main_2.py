import pandas as pd
import numpy as np
from  candidate_group import candidate_group_person
from sklearn.metrics.pairwise import cosine_similarity
from find_n_neighbours import find_n_neighbours
import random

## Read csv
ratings = pd.read_csv(r'C:\Users\guidi\Desktop\universita\Raccomandation System Project\progettoSII_vs\dataset\data.csv', sep=';', names=['user_id', 'movie_id', 'rating', 'timestamp'])
movies = pd.read_csv(r'C:\Users\guidi\Desktop\universita\Raccomandation System Project\progettoSII_vs\dataset\movies.csv', sep=';', names=['movie_id', 'title', 'release_date', 'video_release_date', 'IMDb_url', 'unknown', 'action', 'adventure', 'animation', 'childeren', 'comedy', 'crime', 'documentary', 'drama', 'fantasy', 'film_noir', 'horror', 'musical', 'mystery', 'romance', 'sci_fi', 'thriller','war','western'],  encoding="Latin1")

## Delete column ths is not important
movies.drop(['video_release_date'], axis=1, inplace=True)
movies.drop(['IMDb_url'], axis=1, inplace=True)
movies.drop(['release_date'], axis=1, inplace=True)
     


## normalized
mean = ratings.groupby(by="user_id",as_index=False)['rating'].mean()
rating_avg = pd.merge(ratings,mean,on='user_id')
rating_avg['adg_rating']=rating_avg['rating_x']-rating_avg['rating_y']

## generates two people to recommend the movie
people= candidate_group_person(ratings)

## use cosine similarity for found a Neighbors
check = pd.pivot_table(rating_avg,values='rating_x',index='user_id',columns='movie_id')
check.head()

## first clean a tabel
final=pd.pivot_table(rating_avg,values='adg_rating',index='user_id',columns='movie_id')

## then replace NaN values, and i use the movie average method.
final_movie = final.fillna(final.mean(axis=0))
final_user = final.apply(lambda row: row.fillna(row.mean()), axis=1)


# user similarity on replacing NAN by user avg
b = cosine_similarity(final_user)
np.fill_diagonal(b, 0 )
similarity_with_user = pd.DataFrame(b,index=final_user.index)
similarity_with_user.columns=final_user.index

# user similarity on replacing NAN by item(movie) avg
cosine = cosine_similarity(final_movie)
np.fill_diagonal(cosine, 0 )
similarity_with_movie = pd.DataFrame(cosine,index=final_movie.index)
similarity_with_movie.columns=final_user.index


# top 30 neighbours for each user
sim_user_30_u = find_n_neighbours(similarity_with_user,30)
# print(sim_user_30_u)

def candidate_group_person():
    people = []
    found = True

    while found:
        person_one = random.randint(1, 943)
        person_two = random.randint(1, 943)
        if(person_one != person_two and (ratings['user_id'] == person_one).any() and (ratings['user_id'] == person_two).any()):
            found = False
            people.append(person_one)
            people.append(person_two)

    return people

def find_common_elements(series1, series2):
    common_elements = series1[series1.isin(series2)]
    return common_elements

people = [1,2]
sim_user_30_u1 = sim_user_30_u.iloc[1]
sim_user_30_u2 = sim_user_30_u.iloc[2]
find_neighbors = find_common_elements(sim_user_30_u1, sim_user_30_u2)
while find_neighbors.empty :
    print("sono qui")
    people_new = candidate_group_person()
    people[0] = people_new[0]
    people[1] = people_new[1]
    print(people_new)
    sim_user_30_u1 = sim_user_30_u.iloc[people[0]]
    sim_user_30_u2 = sim_user_30_u.iloc[people[1]]
    find_neighbors = find_common_elements(sim_user_30_u1, sim_user_30_u2)
    
