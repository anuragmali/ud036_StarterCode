import webbrowser

class Movie:
    '''This class is used to create Movie object containing all information
    about one particular movie'''
    
    def __init__(self,movie_title,release_date,story_line,genure,
                 poster_img_url,youtube_trailer_url,rating,cast):
        self.__title = movie_title
        self.__release_date = release_date
        self.__story_line = story_line
        self.__genure = genure
        self.__poster_image_url = poster_img_url
        self.__trailer_youtube_url = youtube_trailer_url
        self.__user_rating = rating
        self.__cast = cast
        
    def show_trailer(self):
        webbrowser.open(self.youtube_trailer_url)

    def get_title(self):
        return self.__title

    def get_release_date(self):
        return self.__release_date

    def get_story_line(self):
        return self.__story_line
    
    def get_genure(self):
        return self.__genure

    def get_poster_image_url(self):
        return self.__poster_image_url

    def get_trailer_youtube_url(self):
        return self.__trailer_youtube_url

    def get_user_rating(self):
        return self.__user_rating

    def get_cast(self):
        return self.__cast

    def set_user_rating(self,rating):
        self.__user_rating = rating

    def set_poster_image_url(self, img_url):
        self.__poster_image_url = img_url

    def set_trailer_youtube_url(self, youtube_url):
        self.__trailer_youtube_url = youtube_url
