"""
* Flask main module
* Responsible for
    - Starting the web server
    - Providing APIs for retrieving movies
    - Rendering views
"""
import ConfigParser
from flask import Flask
from flask import jsonify
from flask import render_template
from MovieRepo import MoviesRepository

app = Flask(__name__, static_url_path='/static')
TMDB_API_KEY = ""


@app.route('/')
def index():
    """Render html file (the view)"""
    return render_template('tomatoes.html')


@app.route('/nowplaying')
def now_playing():
    """Return serialized list of Movie objects"""
    movie_repo = MoviesRepository(TMDB_API_KEY)
    return jsonify([e.serialize() for e in movie_repo.now_playing()])

if __name__ == "__main__":
    """Main entry point"""
    configParser = ConfigParser.RawConfigParser()
    configParser.read(r'config.txt')
    TMDB_API_KEY = configParser.get('TMDB-settings', 'API_KEY')
    if (TMDB_API_KEY == ""):
        print ("Empty API_KEY, please add your API_KEY in config.txt file")
    else:
        app.run()
