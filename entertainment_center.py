"""
Generate Movie objects and store them in memory,
then pass them to fresh_tomatoes module to load
them on a webpage
"""
from media import Movie
import fresh_tomatoes

# Create movie objects
toy_story = Movie(
    "Toy Story",
    "A story of a boy and his toys that come to life",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg")

inside_out = Movie("Inside Out", "Going inside the brain of a young girl",
                   "https://www.youtube.com/watch?v=_MC3XuMvsDI",
                   "http://fontmeme.com/images/inside-out-poster.jpg")

paddington = Movie("Paddington", "A bear finding home in London",
                   "https://www.youtube.com/watch?v=qFuzMlfZGWM",
                   "https://goo.gl/CGddLy")

hidden_figures = Movie("Hidden Figures", "Three women contributing to NASA",
                       "https://www.youtube.com/watch?v=RK8xHq6dfAo",
                       "https://goo.gl/wPurcn")

zootopia = Movie("Zootopia", "A rabbit police officer in Zootopia",
                 "https://www.youtube.com/watch?v=jWM0ct-OLsM",
                 "https://goo.gl/FsK4HE")

moana = Movie("Moana", "A girl from Mawi returning the heart of Tahiti",
              "https://www.youtube.com/watch?v=LKFuXETZUsI",
              "https://goo.gl/tKPBYI")

# store movie objects in memory
movies = [toy_story, inside_out, paddington, hidden_figures, zootopia, moana]

# pass the movie objects to fresh_tomatoes module to display them
# on fresh_tomatoes.html webpage
fresh_tomatoes.open_movies_page(movies)
