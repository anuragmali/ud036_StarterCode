import fresh_tomatoes
import media
import datetime

avatar = media.Movie("Avatar", datetime.datetime(2009,12,18),
                     "best animation movie",
                     ["animation","sci-fi"],
                     "https://upload.wikimedia.org/wikipedia/sco/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY",
                     7.8, ["Sam Worthington","Zoe Saldana","Stephen Lang"])

transporter = media.Movie("The Transporter", datetime.datetime(2009,12,18),
                          "Really good action movie with jason statham performing real action",
                          ["action","thriller"],
                          "https://fanart.tv/fanart/movies/9335/movieposter/transporter-2-562d60f9f259c.jpg",
                          "https://www.youtube.com/watch?v=sYJ5LDoWRT4",
                          6.8, ["Jason Statham","Shu Qi"])

movies = [avatar,transporter]
print(media.Movie.__doc__)
print(type(avatar.release_date))
fresh_tomatoes.open_movies_page(movies)
