"""
Define Movie class to encapsulate movies attributes and methods
"""


class Movie():
    """
    Define attributes and methods associated to Movie objects

    * Attributes:
        title (string): Movie name
        story_line (string): Brief summary of the movie
        trailer_youtube_url (string): link to youtube trailer
        poster_image_url (string): link to movie's poster image
    * Methods:
        __init__
    """

    def __init__(self, movie_name, movie_story_line, movie_youtube_trailer_url,
                 movie_poster_url):
        """Generate a movie object and assign its value"""
        self.title = movie_name
        self.story_line = movie_story_line
        self.trailer_youtube_url = movie_youtube_trailer_url
        self.poster_image_url = movie_poster_url

    # XXXXXXXXXX
    # def show_trailer(self):
    #     webbrowser.open(self.trailer_youtube_url)
