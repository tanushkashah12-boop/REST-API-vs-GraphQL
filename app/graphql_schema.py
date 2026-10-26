import strawberry

from app.data import get_films


@strawberry.type
class Film:
    id: int
    title: str
    director: str
    producer: str
    release_date: str
    running_time: int
    rt_score: int


@strawberry.type
class Query:

    @strawberry.field
    def films(self) -> list[Film]:
        return [Film(**film) for film in get_films()]

    @strawberry.field
    def film(self, id: int) -> Film | None:
        for film in get_films():
            if film["id"] == id:
                return Film(**film)

        return None


schema = strawberry.Schema(query=Query)