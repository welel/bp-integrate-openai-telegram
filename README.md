# Подключаем OpenAI к Telegram Bot

Репозитория для блог поста: Подключаем OpenAI к Telegram Bot

# Разворачиваем проект

Для начала нам нужен проект с телеграм ботом. Вы можете использовать свой проект или сделать клон этого проекта (дальше будем работать в нем): https://github.com/welel/bp-integrate-openai-telegram

1. Клонируем проект

    ```
    git clone git@github.com:welel/bp-integrate-openai-telegram.git
    ```

2. Создаем виртуальное окружение и устанавливаем зависимости

    Подробнее о виртуальном окружении и зависимостях можно узнать в [официальной документации](https%3A%2F%2Fpackaging.python.org%2Fen%2Flatest%2Fguides%2Finstalling-using-pip-and-virtual-environments).

    ```
    # Переходим в дерикторию проекта
    cd bp-integrate-openai-telegram

    # Создаем виртуальное окружение Python 3.10+ 
    python3.10 -m venv env

    # Активируем окружение
    source env/bin/activate

    # Устанавливаем зависимости
    pip install -r requirements.txt
    ```

    *У вас установятся следующие зависимости:*

    ```
    aiogram==3.0.0b7      # Для работы с Telegram
    openai==0.26.5        # Для работы с OpenAI API
    python-dotenv==1.0.0  # Для работы с переменными окружения
    ```

3. Заполняем конфиг

    Предполагается, что вы знаете как создавать нового бота в телеграм и получить токен бота, если нет, то можете прочитать об этом здесь: https://stepik.org/lesson/759381/step/1?unit=761397
    
    В структуре проекта найдите файл под названием `.env.dist` и сделайте копию с названием `.env` рядом. Там будут храниться наши токены. Откройте файл и вставьте туда имеющиеся токены - токен телеграм бота и токен OpenAI.

    ```
    # Telegram Bot Token
    BOT_TOKEN=5497937168:AAHASDAIlWeh4-8jYvo72eZeq23-1P2DQmaY

    # OpenAI Token
    OPENAI_TOKEN=sk-BhC44232lf3VNgLVVADS3BlbkFJtPs00ADSJK21tjPVu7bzl
    ```

    Чтобы проверить работоспособность, запускаем бота:

    ```
    python bot.py
    ```
    
    Если всё работает правильно, то на любое текстовое сообщение в чат с вашим ботом, он будет отвечать "echo".