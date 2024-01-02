# Movie Bot

Hello! MovieBot is a Telegram bot that provides information about movies and also saves the user's search history and 
statistics.

## Description

MovieBot allows users to get the following information about movies:
- Movie description
- Movie rating
- Movie poster

The bot also supports the following functionality:
- Saving user search history
- Tracking user search statistics

## How to Use

1. Send the bot the name of a movie in the chat.
2. The bot will respond with information about the movie, including the description, rating, and poster.

## Команды

- `movie name` - Searches for information about a movie.
- `/history` - Displays the user's search history.
- `/stats` - Displays search statistics for the user.
- `/instruction` or `/help`- Displays available commands.

## Installation and Configuration

- Clone the repository:
```bash
git clone https://github.com/funnydevelopment/cinemaTgBot.git
```
- Create and fill in the contents of the `.env` file following the example in `env.example`.
- Install dependencies:
```bash
cd cinemaTgBot/tgBot
pip install -r requirements.txt
```
- Run the bot:
```bash
python bot.py
```
- For server deployment:
```bash
docker compose build
docker compose up -d
```