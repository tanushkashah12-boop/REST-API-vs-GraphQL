python -m uvicorn app.main:app --reload   

Initializer of sorts

# test in link
http://127.0.0.1:8000/movies
http://127.0.0.1:8000/movies/1
http://127.0.0.1:8000/movies/1/director

returns all 5 movies
movie with id 1
return movie title and director

# Graphql
Concept	Meaning in your project
Type	Defines what fields a movie contains.
Query	Specifies which movie data the client wants.
Resolver	A function that fetches the requested movie data.

# run in graphql to get all 5 movies
{
  allMovies {
    id
    title
    year
    genre
    rating
    director
  }
}

# to get only director and title
{
  allMovies {
    title
    director
  }
}

# to get movie id 1 only title and rating
{
  movie(id: 1) {
    title
    rating
  }
}