'''Module used to create all media objects like movies,songs etc thus by creating entertainment center'''

import fresh_tomatoes
import media
import datetime

#create instances of movies

avatar = media.Movie('Avatar', datetime.datetime(2009,12,18),
                     'best animation movie',
                     ('animation','sci-fi'),
                     'https://upload.wikimedia.org/wikipedia/sco/b/b0/Avatar-Teaser-Poster.jpg',
                     'https://www.youtube.com/watch?v=5PSNL1qE6VY',
                     7.8, ['Sam Worthington','Zoe Saldana','Stephen Lang'])

transporter = media.Movie('The Transporter', datetime.datetime(2009,12,18),
                          'Really good action movie with jason statham performing real action',
                          ('action','thriller'),
                          'https://fanart.tv/fanart/movies/9335/movieposter/transporter-2-562d60f9f259c.jpg',
                          'https://www.youtube.com/watch?v=sYJ5LDoWRT4',
                          6.8, ['Jason Statham','Shu Qi'])

three_idiots = media.Movie('3 Idiots', datetime.datetime(2009,12,25),
                          'Awsome movie in bollywood history describing education system \
                           in India along with love and friendship drama',
                          ('drama','comedy'),
                          'https://upload.wikimedia.org/wikipedia/en/thumb/d/'
                           'df/3_idiots_poster.jpg/220px-3_idiots_poster.jpg',
                          'https://www.youtube.com/watch?v=K0eDlFX9GMc',
                          8.5, ['Aamir Khan','R. Madhavan','Sharman Joshi','Boman Irani','Kareena Kapoor'])

gladiator = media.Movie('Gladiator', datetime.datetime(2000,5,1),
                        'A former Roman General sets out to exact vengeance against \
                        the corrupt emperor who murdered his family and sent him into slavery',
                        ('action','adventure','drama'),
                        'https://upload.wikimedia.org/wikipedia/en/thumb/8/8d'
                         '/Gladiator_ver1.jpg/220px-Gladiator_ver1.jpg',
                        'https://www.youtube.com/watch?v=do9zep1n8cU',
                        8.5, ['Russell Crowe','Joaquin Phoenix','Connie Nielsen','Oliver Reed'])

the_dark_knight = media.Movie('The Dark Knight', datetime.datetime(2008,7,18),
                              'After Gordon, Dent and Batman begin an assault on Gothams organised crime, \
                              the mobs hire the Joker, a psychopathic criminal mastermind, who wants \
                              to bring all the heroes down to his level.',
                              ('action','crime','drama'),
                              'https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg',
                              'https://www.youtube.com/watch?v=EXeTwQWrcwY',
                              9, ['Christian Bale','Heath Ledger','Michael Caine','Gary Oldman'])

wall_E = media.Movie('Wall-E', datetime.datetime(2008,6,21),
                     'A robot who is responsible for cleaning a waste-covered Earth meets \
                     another robot and falls in love with her. Together, they set out on \
                     a journey that will alter the fate of mankind',
                     ('animation','adventure'),
                     'https://upload.wikimedia.org/wikipedia/en/thumb/c/c2/WALL-Eposter.jpg'
                     '/220px-WALL-Eposter.jpg',
                     'https://www.youtube.com/watch?v=8-_9n5DtKOc',
                     8.4, ['Ben Burtt','Elissa Knight','Jeff Garlin'])

#create list of all movie instances
movies = [avatar,transporter,three_idiots,gladiator,the_dark_knight,wall_E]

#pass movies list to create html page rendering movie information
fresh_tomatoes.open_movies_page(movies)
