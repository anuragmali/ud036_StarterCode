import webbrowser

class Movie:
    '''This class is used to create Movie object containing all information
    about one particular movie'''
    
    def __init__(self,movie_title,release_date,story_line,genure,
                 poster_img_url,youtube_trailer_url,rating,cast):
        self.title = movie_title
        self.release_date = release_date
        self.story_line = story_line
        self.genure = genure
        self.poster_image_url = poster_img_url
        self.trailer_youtube_url = youtube_trailer_url
        self.user_rating = rating
        self.cast = cast
        
    def show_trailer(self):
        webbrowser.open(self.youtube_trailer_url)

    
