#### Команды для запуска тестов

Создаем виртуальное окружением любым привычным способом. Например, на windows так:

> py -m venv venv  
> .\venv\Scripts\activate

Устанавливаем необходимые пакеты:

> py -m pip install pytest selenium webdriver-manager

Запускаем все тестовые сценарии:

> pytest
