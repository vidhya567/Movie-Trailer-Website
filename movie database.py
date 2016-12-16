import movie
import fresh_tomatoes
following= movie.Movie("Following","A young writer who follows strangers for material meets a thief who takes him under his wing.","http://torrentking.eu/covers/movies/45/06/0154506.jpg","https://www.youtube.com/watch?v=RHRnYeZL5Pc")
#memento=movie.Movie("Memento","A man juggles searching for his wife's murderer and keeping his short-term memory loss from being an obstacle.","https://wattsatthemovies.files.wordpress.com/2012/11/memento-poster.jpg?w=450&h=400&crop=1","https://www.youtube.com/watch?v=Rq9eM4ZXRgs")
#batmanbegins=movie.Movie("Batman Begins","After training with his mentor, Batman begins his fight to free crime-ridden Gotham City from the corruption that Scarecrow and the League of Shadows have cast upon it.","https://upload.wikimedia.org/wikipedia/en/a/af/Batman_Begins_Poster.jpg","https://www.youtube.com/watch?v=QhPqez3CwiM")
input=open("Memento.txt","r")
row = input.read().splitlines()
moviename=row[0]
storyline=row[1]
imageurl=row[2]
trailerurl=row[3]
memento=movie.Movie(moviename,storyline,imageurl,trailerurl)
input=open("Batman Begins.txt","r")
row = input.read().splitlines()
moviename=row[0]
storyline=row[1]
imageurl=row[2]
trailerurl=row[3]
batmanbegins=movie.Movie(moviename,storyline,imageurl,trailerurl)
prestige=movie.Movie("The Prestige","Two stage magicians engage in competitive one-upmanship in an attempt to create the ultimate stage illusion.","https://s-media-cache-ak0.pinimg.com/originals/b8/ca/36/b8ca36698e80e2e5b8da7ac5311dea68.jpg","https://www.youtube.com/watch?v=DHoXum3M9eE")
darkknight=movie.Movie("The Dark Knight","When the menace known as the Joker wreaks havoc and chaos on the people of Gotham ,the caped crusader must come to terms with one of the greatest psychological tests of his ability to fight injustice.", "https://www.imperialcinema.co.uk/media/filer_public/e4/74/e4742c91-27c7-43b4-b15f-9137437446d0/the-dark-knight-1hroyzdtpgmu7dz4jf22ranzqo7.jpg","https://www.youtube.com/watch?v=TQfATDZY5Y4")
movielist=[following,memento,batmanbegins,prestige]
fresh_tomatoes.open_movies_page(movielist)
