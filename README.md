## Overview
1. Load `files/movies_genres.tsv` into Django using a SQLite database.
1. Create a JSON REST API following the criteria below.

### API Functionality
The API should be able to:
1. create, retrieve, list, update, and delete `movies` and `genres`
1. filter `movies` by `genre`
1. retrieve and list counts of `movies` by `genre`

### Advanced API Functionality
The API should be able to:
1. retrieve or list which genre had the most movies per year.  The returned data should include the year, genre name, and count.
2. retrieve or list movies that include a "number of sequels" field based on whether this movie name is a prefix of other movies.  For example, "The Godfather" is a prefix of "The Godfather Part II" and "The Godfather Part III", so the REST endpoint for "The Godfather" should show a sequel count of 2.  
    * Note, you can add this to the existing "movies" REST API from the core API you wrote above.

### Testing
Be sure to write tests for your code, and document as needed.  Feel free to add anything else that you believe improves the maintainability of the project.

## Submission
Once you're complete, upload your code to a public git repository and send us a link.  We will clone and test your solution locally.  Be sure to include any relevant commands and/or instructions on how to load the data and access the API.
