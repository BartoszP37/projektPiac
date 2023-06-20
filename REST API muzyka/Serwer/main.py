from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api=Api(app)

class songs(Resource):
    def get(self):
        songs = [
    {
        'id': 1,
        'wykonawca': 'Endless Summer',
        'tytuł': 'Crying On The Dancefloor',
        'czas': '3:09',
        'format': 'MP3'
    },
    {
        'id': 2,
        'wykonawca': 'Queen',
        'tytuł': 'Bohemian Rhapsody',
        'czas': '5:55',
        'format': 'MP3'
    },
    {
        'id': 3,
        'wykonawca': 'Michael Jackson',
        'tytuł': 'Thriller',
        'czas': '5:57',
        'format': 'MP3'
    },
     {
        'id': 4,
        'wykonawca': 'Imagine Dragons',
        'tytuł': 'Enemy',
        'czas': '3:33',
        'format': 'MP3'
    }
    
]
        return songs
    
api.add_resource(songs, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=88 )
