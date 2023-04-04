# Django QUIZ

[![Testing](https://github.com/d1squit/django_quiz/actions/workflows/test.yml/badge.svg)](https://github.com/python-hillel/django_quiz_1/actions/workflows/test.yml)

## Технические требования  
### Web-UI
  1. Регистрация
      - [x] регистрация (с подтверждением по email)
      - [x] авторизация
      - [x] смена пароля
      - [x] сброс пароля
    
  2. Возможности пользователя
      - [x] прохождение любого теста
      - [x] последовательно проходить вопросы теста (один за другим)
      - [x] завершение отложенного теста
      - [x] удаление незавершенного теста 
      - [x] просмотр результатов
    
  3. После завершения теста
      - [x] двухцветный ProgressBar с процентом правильных и неправильных ответов

### Admin site
  1. [x] Управление пользователями
  2. [x] Управление тестами
      - [x] добавление теста
      - [x] изменить тест
      - [x] удаление теста
      - [x] валидация теста
        - [x] нельзя сохранить вопрос:
            - [x] без указания правильного ответа
            - [x] в которых все ответы правильные
        - [x] нельзя сохранить тест если:
            - [x] некорректный order_num (должен быть от 1 до 100 и увеличиваться на 1)
            - [x] максимальное значение order_num не более максимально допустимого кол-ва вопросов
            - [x] кол-во вопросов менее 3 или более 100

### Дополнительные требования
1. [x] Проект должен быть на Git-е
2. [x] Наличие файла requirements.txt
3. [x] venv
4. [ ] PostgreSQL
5. [x] Наличие дампа данных
6. [x] bootstrap
7. [x] Unit Tests
8. [ ] Docker image
9. [ ] Деплой на Amazon
10. [ ] Планировщик
11. [ ] Кэширование


ext.: [ ] API + Tests

## DB - Schema
![db](db_schema.png)