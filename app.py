from flask import Flask, redirect, url_for, render_template
import requests
import json

app = Flask(__name__)

API_KEY = ''
BASE_URL = 'https://api.brawlstars.com/v1'
PLAYER_TAG = '%238YY8Q8GRR'
params = dict(authorization="Bearer {}".format(API_KEY))

newthing = requests.get(BASE_URL + 'players/' + PLAYER_TAG, params)
res = newthing.content

@app.route('/')
def index():
    req = requests.get(BASE_URL + '/brawlers', params)
    res = json.loads(req.content)
    names = []
    for item in res['items']:
        names.append(item['name'])
    return render_template("index.html", names=names)

@app.route('/profile')
def profile():
    req = requests.get(BASE_URL + '/players/' + PLAYER_TAG, params)
    res = json.loads(req.content)
    stats = {
        "trophies": res['trophies'],
        "highest_trophies": res['highestTrophies'],
        "power_play_points": res['powerPlayPoints'],
        "highest_power_play_points": res['highestPowerPlayPoints'],
        "exp_level": res['expLevel'],
        "exp_points": res['expPoints'],
        "3vs3_victories": res['3vs3Victories'],
        "solo_victories": res['soloVictories'],
        "duo_victories": res['duoVictories'],
        "best_robo_rumble_time": res['bestRoboRumbleTime'],
        "best_time_as_big_brawler": res['bestTimeAsBigBrawler']
    }
    return render_template("profile.html", stats=stats)

@app.route('/player-brawlers')
def player_brawlers():
    req = requests.get(BASE_URL + '/players/' + PLAYER_TAG, params)
    res = json.loads(req.content)
    names = []
    for brawler in res['brawlers']:
        names.append(brawler['name'])
    return render_template("player-brawlers.html", names=names)

if __name__ == "__main__":
    app.run(debug=True)