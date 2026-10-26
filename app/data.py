from functools import lru_cache

import requests

GHIBLI_API_URL = "https://ghibliapi.vercel.app/films"


@lru_cache(maxsize=1)
def get_films():
    """Fetch films once and cache the result."""

    response = requests.get(
        GHIBLI_API_URL,
        params={
            "limit": 10,
            "fields": (
                "id,title,director,producer,"
                "release_date,running_time,rt_score"
            ),
        },
        timeout=15,
    )
    response.raise_for_status()

    api_films = response.json()

    # Assign simple local IDs from 1 to 10.
    films = []
    for local_id, film in enumerate(api_films[:10], start=1):
        films.append({
            "id": local_id,
            "title": film["title"],
            "director": film["director"],
            "producer": film["producer"],
            "release_date": film["release_date"],
            "running_time": int(film["running_time"]),
            "rt_score": int(film["rt_score"]),
        })

    return films
