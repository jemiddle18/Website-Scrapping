import requests #imported to pull down website
from bs4 import BeautifulSoup
 
web_page = requests.get('https://editorial.rottentomatoes.com/guide/all-marvel-cinematic-universe-movies-ranked/') # Getting page HTML through request
soup = BeautifulSoup(web_page.content, 'html.parser') # Parsing content using beautifulsoup

Movie_list = soup.find_all('div', class_='article_movie_title') # The title of the Div class is Article_movie_title, so searching for it as such.
Movie_rating = soup.find_all('div', class_='countdown-index') # The rating for the movies are stored in this div class.

for movie in Movie_list: # For loop to filter through lists of movies.
    movie_name = movie.a.text #The name of the movie is stored in the 'a' attribute.
    movie_rating = movie.text # Pulling out the text for the Movie rating on rotten tomatoes
    print(movie_name) # Printing out the list of Marvel Movies
    print(movie_rating) # Printing out movie rating assoicated with the following movie.

