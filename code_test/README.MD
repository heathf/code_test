This Django app will obtain movie information, as well as genre information related to the movies.  You can GET, POST,
PUT and DELETE both movies and genres.  You can also get which genre had the most movies made for a given year, and
obtain the sequels for a given movie.  Some examples of using the API are below:

EXAMPLES:

    Example of getting genres by year with curl.
    
    curl "http://127.0.0.1:8000/code_test/genres/47/get-most-genres-year/?year=2012"


    Example of obtaining the number of sequels for a given movie:

    curl "http://127.0.0.1:8000/code_test/movies/1299/get-number-of-sequels/“


    Example getting a movie by name:

    curl "http://127.0.0.1:8000/code_test/movies/?name=Avery%20Park”