import youtube
import media
import fresh_tomatoes

list = youtube.Youtube()
list.search = "movie trailer" # What is interesting topic? 'funny pet'? 'cute kitten'? 'Udacity'?
list.load()

movies = []
youtube_prefix = 'https://www.youtube.com/watch?v='
# Mapping youtube API response to our movie array
for item in list.data['items']:
	title = item['snippet']['title']
	storyline = item['snippet']['description']
	video = youtube_prefix + item['id']['videoId']
	poster_image_url = item['snippet']['thumbnails']['high']['url']
	movies.append(media.Movie(title, storyline, poster_image_url, video))

# Rendering page
fresh_tomatoes.open_movies_page(movies)