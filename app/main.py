from fastapi import FastAPI, HTTPException, Query
from strawberry.fastapi import GraphQLRouter

from app.data import get_films
from app.graphql_schema import schema

app = FastAPI(
    title="Studio Ghibli: REST vs GraphQL",
    description="Read-only API comparison project",
    version="1.0.0",
)


@app.get("/films", tags=["REST"])
def list_films(
    fields: str | None = Query(
        default=None,
        description="Optional comma-separated fields",
    )
):
    films = get_films()

    if not fields:
        return films

    requested = {field.strip() for field in fields.split(",")}
    allowed = set(films[0].keys())
    invalid = requested - allowed

    if invalid:
        raise HTTPException(
            status_code=400,
            detail=f"Unknown fields: {', '.join(sorted(invalid))}",
        )

    return [
        {key: value for key, value in film.items()
         if key in requested}
        for film in films
    ]


@app.get("/films/{film_id}", tags=["REST"])
def get_film(film_id: int):
    for film in get_films():
        if film["id"] == film_id:
            return film

    raise HTTPException(status_code=404, detail="Film not found")


@app.get("/films/{film_id}/director", tags=["REST"])
def get_film_director(film_id: int):
    for film in get_films():
        if film["id"] == film_id:
            return {
                "id": film["id"],
                "title": film["title"],
                "director": film["director"],
            }

    raise HTTPException(status_code=404, detail="Film not found")


graphql_router = GraphQLRouter(schema)
app.include_router(graphql_router, prefix="/graphql")