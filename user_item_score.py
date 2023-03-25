import sys
import pandas as pd

def User_item_score(user,item, sim_user_30_m, mean, final_movie, similarity_with_movie):
    a = sim_user_30_m[sim_user_30_m.index==user].values
    b = a.squeeze().tolist()
    c = final_movie.loc[:,item]
    print("C", c)
    d = c[c.index.isin(b)]
    f = d[d.notnull()]
    avg_user = mean.loc[mean['user_id'] == user,'rating'].values[0]
    index = f.index.values.squeeze().tolist()
    corr = similarity_with_movie.loc[user,index]
    fin = pd.concat([f, corr], axis=1)
    fin.columns = ['adg_score','correlation']
    fin['score']=fin.apply(lambda x:x['adg_score'] * x['correlation'],axis=1)
    nume = fin['score'].sum()
    deno = fin['correlation'].sum()
    final_score = avg_user + (nume/deno)
    return final_score

sys.modules[User_item_score] = User_item_score