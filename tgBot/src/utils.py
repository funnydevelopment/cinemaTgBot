from common.exceptions import ElementIndexError


async def create_movie_list(data) -> str:
    movie_list = ""
    try:
        for el in data:
            movie_list += f"- {el[1]}\n"
    except ElementIndexError:
        pass
    return movie_list
