##### Data preprocessing scirpt


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
import time
from tqdm import tqdm

def fantasy_points(df):
  all_points = []
  for i,row in df.iterrows():
    player_points = 0
    player_points += 0.1 * (row['rush_yds'] + row['rec_yds'])
    player_points += 6 * (row['rush_td'] + row['rec_td'])
    player_points += (1/25) * row['pass_yds']
    player_points += (4) * row['pass_td']
    player_points += (-2) * row['int']
    player_points += (-2) * row['fumbles']
    all_points.append(player_points)
  return all_points

def attach_dummies(df):
  
def combine_df(df_list):

def load_years(years):
  ## years: list of years
  

    