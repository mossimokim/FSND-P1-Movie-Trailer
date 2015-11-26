#Youtube viewer is written as a part of Udacity Full Stack Web Developer Nanodegree Course
It dynamically populate and generate a page by data queried from youtube API by given topic.
Default topic is "Movie Trailer", sorted by view count, but feel free to change in entertainment_center.py


#Quickstart:

Make sure python 2.7 is installed
Install python JSON & REQUEST module if you don't have yet
(refer to http://docs.python-requests.org/en/latest/user/install/#install) for instructions
Download viewer.zip and unpack
Update youtube API key with your own key in youtube.py
run entertainment.py which will generate "fresh_tomatoes.html"
Enjoy!


#List of files included:

entertainmnet_center.py
fresh_tomatoes.py
media.py
youtube.py


#Creator & Support Contact:

Daniel Kim (mossimokim@gmail.com)
https://profiles.udacity.com/u/danielkim1


#Note to the Reviewer:

IMDB API is lacking documentation due to legal issue.
OMDB API lacks features
Rotten Tomatoes API is complete, but I did not want to embed their videos due to excessive commercials.
Minor CSS changes to make pages look better.. fixed floating box issues when title gets too long.
Tooptip is added for the unused description(storyline) on image hover.
