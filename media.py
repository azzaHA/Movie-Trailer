"""
Define Movie class to encapsulate movies attributes and methods
"""


class Movie():
    """
    Define attributes and methods associated to Movie objects

    * Attributes:
        title (string): Movie name
        story_line (string): Brief summary of the movie
        trailer_youtube_id (string): trailer ID on youtube
        poster_image_url (string): link to movie's poster image
    * Methods:
        __init__: instantiates a new Movie object with passed arguments
        serialize: serializes Movie object to its JSON representation
    """

    def __init__(self, movie_name, movie_story_line, movie_youtube_trailer_id,
                 movie_poster_url):
        """Generate a movie object and assign its value"""
        self.title = movie_name
        self.story_line = movie_story_line
        self.trailer_youtube_id = movie_youtube_trailer_id
        self.poster_image_url = movie_poster_url

    def serialize(self):
        """serialize Movie object to its JSON representation"""
        return{
            'title': self.title,
            'story_line': self.story_line,
            'trailer_youtube_id': self.trailer_youtube_id,
            'poster_image_url': self.poster_image_url
        }
