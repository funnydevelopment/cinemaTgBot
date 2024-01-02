HELLO_TEXT = (
    "Hello, {user_name}!\n"
    "I'm here to help you find movies. Just enter the movie title, and I'll do my best "
    "to locate that movie!\n\n"
    "For additional information, type the command <b><i>/help</i></b> "
    'or click the <b><i>"Instructions"</i></b> button.'
)

HELP_TEXT = (
    "This bot finds movies, provides descriptions, posters, and ratings.\n"
    "It also keeps a search history and maintains statistics.\n\n"
    "The list of available commands:\n"
    "<b><i>/start</i></b> - to restart the bot\n"
    "<b><i>/help</i></b> - to get detailed information\n"
    "<b><i>/stats</i></b> - to get statistics\n"
    "<b><i>/history.</i></b> - to get search history"
)

STATS_TEXT = "Number of user requests: <b><u>{total_count}.</u></b>"

HISTORY_TEXT = "User history: {user_name}.\n"

SEARCH_RESULT_TEXT = (
    "Title📍: <b><i>{name}</i></b>\n\n"
    "Rating🔎: <b><i>{rating}</i></b>\n\n"
    "Overview📝: <i>{overview}</i>\n\n"
    "Watch trailer🖼: <i>{link}</i>"
)

FAILED_RESULT_TEXT = (
    "Sorry, we couldn't find anything matching your query. Try adjusting your "
    "search criteria."
)
