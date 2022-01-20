# Spotify-music-skip-prediction(https://spotify-music-skip-pediction.herokuapp.com/)
  I worked in Spotify music skip action prediction as an internship project. spotify  has over 190 million active users interacting with over 40 million tracks.
  
##Features

In this project track_features data and training data. track_features data containing 3757092 raws and 30 columns.
track_id                  
duration                  
release_year              
us_popularity_estimate    
acousticness              
beat_strength             
bounciness                
danceability              
dyn_range_mean            
energy                    
flatness                  
instrumentalness          
key                       
liveness                  
loudness                  
mechanism                 
mode                      
organism                  
speechiness               
tempo                     
time_signature            
valence                   
acoustic_vector_0         
acoustic_vector_1         
acoustic_vector_2         
acoustic_vector_3         
acoustic_vector_4         
acoustic_vector_5         
acoustic_vector_6         
acoustic_vector_7         

In training data set Containig 167880 raws and 21 columns

session_id                         
session_position                   
session_length                     
track_id_clean                     
skip_1                             
skip_2                             
skip_3                             
not_skipped                        
context_switch                     
no_pause_before_play               
short_pause_before_play            
long_pause_before_play             
hist_user_behavior_n_seekfwd       
hist_user_behavior_n_seekback      
hist_user_behavior_is_shuffle      
hour_of_day                        
date                               
premium                            
context_type                       
hist_user_behavior_reason_start    
hist_user_behavior_reason_end      

After loading these dataset,then merge the dataset track_ features and training features.

Data Analysis

1 Find Unwanted Columns

2 Find Missing Values

3 Find Features with one value

4 Explore the Categorical Features

5 Find Categorical Feature Distribution

6 Relationship between Categorical Features and Label

7 Explore the Numerical Features

8 Find Discrete Numerical Features

9 Relation between Discrete numerical Features and Labels

10 Find Continous Numerical Features

11 Distribution of Continous Numerical Features

12 Relation between Continous numerical Features and Labels

13 Find Outliers in numerical features

14 Explore the Correlation between numerical features

Feature Engingineering

Drop unwanted features

Handle missing value

Handle categorical features

Handle feature scaling

Later applying Pca on this project

Model Development

 Logistic regression
 Decision Tree Classifier
 Random forest
 Xgboost
 
 
The ML model for the problem statement was created using python with the help of the dataset, and the ML model created with Random Forest and DecisiontreeClassifier models performed better than Logistics Regression model. Thus, for the given problem, the models created by Random Forest and DecisiontreeClassifier.

Later making streamlit app and it predict if the music is skipped or not skipped. Then it deployed in to Heroku.


 




