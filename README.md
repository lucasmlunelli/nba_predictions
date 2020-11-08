# NBA Predictions

Machine learning model to predict NBA games winners and the creation of betting strategies to profit from the model's results.

Code:
scrapper/match_generator.py -> Basketball Reference crawler; creates a json file for each game (data/data_raw) <br>
ETL.yxmd -> Alteryx file with ETL process; extract game logs (data/data_raw), transform data with feature engineering and load it in SQLite database (data/data_transformed) <br>
Machine Learning.ipynb -> Jupyter notebook with machine learning models; uses SQLite database as input <br>
Betting System.xlsx -> Excel with parameters to create all the betting strategies and simulate the results; uses ML results as input <br>

Data:
  data_raw -> json files with stats from each game created using scrapper/match_generator.py <br>
  data_transformed -> SQLite database; created using ETL.yxmd file
