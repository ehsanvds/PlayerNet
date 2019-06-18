from flask import render_template, request 
from flaskexample import app
import os
import pandas as pd

@app.route('/', methods=['GET','POST'])
def index():
    return render_template("index.html")

@app.route('/players',  methods=['GET','POST'])
def player_page():
    output=""
    error=""
    name0=""
    name1=""
    name2=""
    url0=""
    url1=""
    url2=""
    img0=""
    img1=""
    img2=""
    sel_genre=""
    
    dict_genres = {'1': 'Action', '37': 'Free to Play', '2': 'Strategy', '25': 'Adventure', '23': 'Indie', '3': 'RPG', '4': 'Casual', '28': 'Simulation', '9': 'Racing', '29': 'Massively Multiplayer', '18': 'Sports', '70': 'Early Access'}    
    
    input = '.../players_cent_score.csv'
    data = pd.read_csv(os.path.join(input))
    
    input_genre = int(request.form['genre'])
    
    if input_genre == -1:
        error = True
    if input_genre != -1:
        data = data.sort_values(dict_genres[str(input_genre)], ascending=False).iloc[0:3,:]
        sel_genre = dict_genres[str(input_genre)]
        output = True
    
    # account ID and URLs
    name0=', # of Friends: ' + str(data.iloc[0,1])
    name1=', # of Friends: ' + str(data.iloc[1,1])
    name2=', # of Friends: ' + str(data.iloc[2,1])
    url0='https://steamcommunity.com/profiles/' + str(data.iloc[0,0])
    url1='https://steamcommunity.com/profiles/' + str(data.iloc[1,0])
    url2='https://steamcommunity.com/profiles/' + str(data.iloc[2,0])
    img='https://upload.wikimedia.org/wikipedia/commons/8/83/Steam_icon_logo.svg'
    
    return render_template("index.html",output=output,error_page=error,name0=name0,name1=name1,name2=name2,url0=url0,url1=url1,url2=url2,img=img,sel_genre=sel_genre)