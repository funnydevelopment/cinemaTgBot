# Movie Bot

Привет! MovieBot - это Telegram бот, который предоставляет информацию о фильмах, а также сохраняет историю поиска и статистику пользователя.

## Описание

MovieBot позволяет пользователям получать следующую информацию о фильмах:
- Описание фильма
- Рейтинг фильма
- Постер фильма

Бот также поддерживает следующий функционал:
- Сохранение истории поиска пользователя
- Отслеживание статистики поисков пользователя

## Как использовать

1. Отправьте боту название фильма в чат.
2. Бот ответит информацией о фильме, включая описание, рейтинг и постер.

## Команды

- `название фильма` - Ищет информацию о фильме.
- `/history` - Выводит историю поиска пользователя.
- `/stats` - Выводит статистику поиска пользователя.

## Установка и настройка

- Клонируйте репозиторий:
```bash
git clone https://github.com/ funnydevelopment/cinemaTgBot.git
```
- Установите зависимости:
```bash
cd cinemaTgBot/tgBot
pip install -r requirements.txt
```
- Запустите бота:
```bash
python bot.py
```