import pandas as pd
import numpy as np
from sklearn.ensemble import  RandomForestClassifier
from sklearn.model_selection import train_test_split
import warnings
import pickle
#import streamlit as st
warnings.filterwarnings("ignore")

tf_data = pd.concat(map(pd.read_csv, ['tf_000000000001.csv', 'tf_mini (1).csv.gz','tf_000000000000.csv']), ignore_index=True)

tr_data=pd.read_csv("log_mini.csv.gz")

# Using skip_2 as the ground truth
tr_data['skipped'] = (tr_data.skip_2 & tr_data.skip_1).astype('int32')
tr_data = tr_data.drop(columns=['skip_1','skip_2','skip_3','not_skipped'])
tr_data.head()

# Join the two together
df = (
    tr_data
    .merge(
        tf_data,
        how='left',
        left_on=['track_id_clean'],
        right_on=['track_id']
    ).drop(columns='track_id_clean')
)
df.head()


#Convert the object values to numerical values
from sklearn.preprocessing import LabelEncoder
le1=LabelEncoder()
df['session_id']=le1.fit_transform(df['session_id'])

le2=LabelEncoder()
df['hist_user_behavior_is_shuffle']=le2.fit_transform(df['hist_user_behavior_is_shuffle'])

le3=LabelEncoder()
df['date']=le3.fit_transform(df['date'])

le4=LabelEncoder()
df['premium']=le4.fit_transform(df['premium'])

le5=LabelEncoder()
df['context_type']=le5.fit_transform(df['context_type'])

le6=LabelEncoder()
df['hist_user_behavior_reason_start']=le6.fit_transform(df['hist_user_behavior_reason_start'])

le7=LabelEncoder()
df['hist_user_behavior_reason_end']=le7.fit_transform(df['hist_user_behavior_reason_end'])

le8=LabelEncoder()
df['track_id']=le8.fit_transform(df['track_id'])

le9=LabelEncoder()
df['mode']=le9.fit_transform(df['mode'])

df1=df.drop(['hist_user_behavior_reason_end','hist_user_behavior_reason_start','session_id',
             'long_pause_before_play','short_pause_before_play','hist_user_behavior_n_seekback',
             'hist_user_behavior_n_seekfwd','acoustic_vector_0','acoustic_vector_6','acousticness','acoustic_vector_1',
             'acoustic_vector_4','instrumentalness','organism','release_year','mechanism','acoustic_vector_3',
             'acoustic_vector_5','acoustic_vector_7','acoustic_vector_2','flatness','speechiness','liveness','key',
             'danceability'],axis=1)

#splitting the data
X = df1.drop(columns=["skipped"]).fillna(-9999)
y=df1.skipped

#df1=np.array(df)


X_train,X_test,y_train,y_test=train_test_split(X,y,train_size=0.75,random_state=0)




from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(X_train)
x_test=sc.fit_transform(X_test)


from sklearn.linear_model import LogisticRegression
lg_model=LogisticRegression()
lg_model.fit(X_train,y_train)
pred=lg_model.predict(X_test)

from sklearn.metrics import  accuracy_score
acc=accuracy_score(y_test,pred)

#fitting and trining dataset in to random forest model
from sklearn.ensemble import RandomForestClassifier
rf_model=RandomForestClassifier(criterion="gini",n_estimators=10,random_state=1)

rf_model.fit(X_train,y_train)

rf_pred=rf_model.predict(X_test)
from sklearn.metrics import  accuracy_score
acc1=accuracy_score(y_test,rf_pred)

#Apply decision tree Algorithm
from sklearn.tree import DecisionTreeClassifier
dt_model=DecisionTreeClassifier(criterion="entropy")
dt_model.fit(X_train,y_train)

dt_pred=dt_model.predict(X_test)
from sklearn.metrics import  accuracy_score
acc2=accuracy_score(y_test,dt_pred)




import pickle
f1=open(file="rf_model.pkl",mode="wb")
pickle.dump(rf_model,f1)
f1.close()

f2=open(file="lg_model.pkl",mode="wb")
pickle.dump(lg_model,f2)
f2.close()

f3=open(file="dt_model.pkl",mode="wb")
pickle.dump(dt_model,f3)
f3.close()


