import pandas as pd
import numpy as np
from  candidate_group import candidate_group_person
from sklearn.metrics.pairwise import cosine_similarity
from find_n_neighbours import find_n_neighbours
from user_item_score1 import User_item_score1
from user_item_score import User_item_score

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
print(people)

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



# top 30 neighbours for each user
sim_user_30_m = find_n_neighbours(similarity_with_movie,30)



def get_user_similar_movies( user1, user2 ):
    common_movies = rating_avg[rating_avg.user_id == user1].merge(
    rating_avg[rating_avg.user_id == user2],
    on = "movie_id",
    how = "inner" )
    return common_movies.merge( movies, on = 'movie_id' )

a = get_user_similar_movies(370,86309)
a = a.loc[ : , ['rating_x_x','rating_x_y','title']]
# pd.DataFrame(a)
# print(a)



score = User_item_score(320,7371, sim_user_30_m, mean, final_movie, similarity_with_movie)
print("score (u,i) is",score)

rating_avg = rating_avg.astype({"movie_id": str})
movie_user = rating_avg.groupby(by = 'user_id')['movie_id'].apply(lambda x:','.join(x))



predicted_movies = User_item_score1(people[1], sim_user_30_m, movie_user, final_movie, mean, similarity_with_movie, movies, check)
print(" ")
print("The Recommendations for User Id : 370")
print("   ")
for i in predicted_movies:
    print(i)