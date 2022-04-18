import requests #imported to pull down website
import pymongo # import for mongo Database. Will be used to add movies into it.

from bs4 import BeautifulSoup
 
web_page = requests.get('https://editorial.rottentomatoes.com/guide/all-marvel-cinematic-universe-movies-ranked/') # Getting page HTML through request
soup = BeautifulSoup(web_page.content, 'html.parser') # Parsing content using beautifulsoup
dbclient = pymongo.MongoClient("mongodb://localhost:27017/") # Create database
mydb = dbclient["mydatabase"] # Naming the database for usage.
collection = mydb["Movies"]

Movie_list = soup.find_all('div', class_='article_movie_title') # The title of the Div class is Article_movie_title, so searching for it as such.
Movie_rating = soup.find_all('div', class_='countdown-index') # The rating for the movies are stored in this div class.

for movie in Movie_list: # For loop to filter through lists of movies.
    movie_name = movie.a.text #The name of the movie is stored in the 'a' attribute.
    movie_rating = movie.text # Pulling out the text for the Movie rating on rotten tomatoes
    movie_table = { "Name": movie_name, "Rating": movie_rating}
    
print(movie_table)