# predictor
Using EPL Results to predict the scores of upcoming EPL Games

Current State: Parsing the upcoming games from 538
               Developing the data structures used to hold necessary statistics about each team
               
Future State:
               Use statistics to create one hot vectors for each team. Using logistical regression, train on the existing results and                    weight the vectors so they can be used to predict future games. Aim to retrain data each week using the additional week of                results and see if the predictions get better week by week. 


