HELLO_TEXT = (
    "Здравствуйте, {user_name}!\n"
    "Я здесь, чтобы по поиску фильмов. Просто введите название фильма, а я постараюсь "
    "найти этот фильм!\n\n"
    "Для получения дополнительной информации введите команду <b><i>/help</i></b> "
    'или нажмите на кнопку <b><i>"Инструкция"</i></b>.'
)

HELP_TEXT = (
    "Данный бот находит фильм, описание, постер и рейтинг.\n"
    "Также бот записывает историю поиска и ведет статистику."
)

STATS_TEXT = "Количество запросов пользователя: {user_name}."

HISTORY_TEXT = "История пользователя: {user_name}.\n"

SEARCH_RESULT_TEXT = (
    "Title: <b><i>{name}</i></b>\n"
    "Rating: <b><i>{rating}</i></b>\n"
    "Overview: <i>{overview}</i>\n"
    "Watch trailer: <i>{link}</i>"
)

FAILED_RESULT_TEXT = (
    "Sorry, we couldn't find anything matching your query. Try adjusting your "
    "search criteria."
)
