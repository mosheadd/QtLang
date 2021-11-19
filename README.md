# Пояснительная записка. Бабич Ростислав.
# Проект по компьютерной лингвистике.
 
## Программа включает в себя.
- База данных языков и морфологические анализы.

Базы данных реализованы следующим образом:
Каждый язык - отдельная база, в которой хранятся таблицы - данные об языке.
1. Слова
2. Морфемы
3. Алфавит/письменность
4. Падежи
5. Части речи
6. Классификация

Реализован полный интерфейс работы с базой данных.
* Просмотр таблиц.
* Изменение таблиц.
* Получение данных из таблиц.

Морфологический разбор слова.
Пользователь вводит язык, само слово и часть речи. Анализ возвращает морфемы слова и его характеристику: морфемы(части слова), число, род, и написание в МФА. Полученные данные о слове можно записать в язык специальной кнопкой.

Присутствует прототип анализа текста, который только выводит кол-во введённых слов (другие символы, кроме букв языка, не считаются).

Есть главное меню и к каждой кнопке прикрепленны горячие клавишы.

Использованные технологие:
- Соответсвенно сам Python
- Sqlite3
- PyQt5