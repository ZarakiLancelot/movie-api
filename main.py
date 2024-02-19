from fastapi import FastAPI, HTTPException, Path, Query
from fastapi.responses import JSONResponse
from models.movie import Movie

app = FastAPI()
app.title = "Movies API"
app.version = "0.0.1"

movies = [
    {'id': 1, 'title': 'The Shawshank Redemption', 'release_year': 1994, 'category': 'Drama', 'rating': 9.3},
    {'id': 2, 'title': 'The Godfather', 'release_year': 1972, 'category': 'Drama', 'rating': 9.2},
    {'id': 3, 'title': 'The Dark Knight', 'release_year': 2008, 'category': 'Action', 'rating': 9.0},
]


@app.get('/', tags=['home'])
def alive():
    return {'Hello': 'World'}

@app.get('/movies', tags=['movies'], response_model=list[Movie])
async def get_movies() -> list[Movie]:
    return JSONResponse(content=movies)

@app.get('/movies/{id}', tags=['movies'], response_model=Movie)
async def get_movie(id: int = Path(ge=1, le=2000)) -> Movie:
    return JSONResponse(movies[id - 1] if 1 <= id <= len(movies) else {'error': 'Movie with ID %i not found.' % (id)})

@app.get('/movies/', tags=['movies'], response_model=list[Movie])
async def get_movies_by_category(category: str, release_year: int = None) -> list[Movie]:
    return JSONResponse([movie for movie in movies if movie['category'] == category and (release_year is None or movie['release_year'] == release_year)])

@app.post('/movies', tags=['movies'], response_model=Movie)
async def add_movie(movie: Movie):
    movies.append(movie.model_dump())
    return JSONResponse(content={'message': 'Movie added'})

@app.put('/movies/{id}', tags=['movies'], response_model=Movie)
async def update_movie(id: int, movie: Movie):
    if 1 <= id <= len(movies):
        movies[id - 1] = movie.model_dump()
        return JSONResponse(content={'message': 'Movie updated'})
    else:
        raise HTTPException(status_code=404, detail="Movie not found")
    
@app.patch('/movies/{id}', tags=['movies'], response_model=Movie)
async def patch_movie(id: int, movie: Movie):
    if 1 <= id <= len(movies):
        movies[id - 1] = movie.model_dump(exclude_unset=True)
        return JSONResponse(content={'message': 'Movie updated'})
    else:
        raise HTTPException(status_code=404, detail="Movie not found")

@app.delete('/movies/{id}', tags=['movies'])
async def remove_movie(id: int):
    if 1 <= id <= len(movies):
        movies.pop(id - 1)
        return JSONResponse(content={'message': 'Movie removed'})
    else:
        raise HTTPException(status_code=404, detail="Movie not found")
