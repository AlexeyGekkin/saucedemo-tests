# Автоматический тест для Saucedemo

Этот проект содержит автоматический тест для проверки процесса покупки товара на сайте Saucedemo с использованием Python и Selenium. Тест выполняет авторизацию, добавление товара в корзину и оформление покупки.

## Требования

1. **Python**: Убедитесь, что на вашем компьютере установлен Python версии 3.6 или выше.
2. **Интернет-соединение**: Необходимо для загрузки зависимостей и доступа к сайту.
3. **Браузер**: Тест использует браузер Google Chrome. Браузер должен быть установлен на вашем компьютере.

## Инструкции по установке и запуску

1. **Установите Python**:
   - Скачайте и установите Python с [python.org](https://www.python.org/downloads/).
   - Убедитесь, что Python добавлен в PATH вашей системы во время установки.

2. **Клонируйте репозиторий**:
   - Перейдите в рабочую папку, например:
     ```bash
     cd d:\dev
     ```
   - Клонируйте репозиторий с кодом теста с GitHub:
     ```bash
     git clone https://github.com/AlexeyGekkin/saucedemo-tests.git
     cd saucedemo-tests
     ```

4. **Создайте виртуальное окружение** (опционально, но рекомендуется):
   - Создайте виртуальное окружение для управления зависимостями:
     ```bash
     python -m venv venv
     ```
   - Активируйте виртуальное окружение:
     - **Windows**:
       ```bash
       venv\Scripts\activate
       ```
     - **macOS/Linux**:
       ```bash
       source venv/bin/activate
       ```

5. **Установите зависимости**:
   - Установите необходимые Python-пакеты:
     ```bash
     pip install -r requirements.txt
     ```
6. **Запустите тест**:
   - Выполните тестовый скрипт с помощью Python:
     ```bash
     python ваш_тестовый_скрипт.py
     ```

## Описание теста

Скрипт выполняет следующие шаги:
1. **Авторизация**: Выполняет вход на сайт с использованием предоставленного имени пользователя и пароля.
2. **Добавление товара в корзину**: Добавляет указанный товар в корзину.
3. **Оформление покупки**: Завершает процесс покупки.
     
