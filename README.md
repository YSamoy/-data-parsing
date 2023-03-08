<h1 align="center">Методы сбора и обработки данных из сети Интернет</h1>

Geek University Data Science

<strong>Python MongoDB API SOAP JSON XPath</strong>

В данном курсе были выполнены следующие задания.

Урок 1. Основы клиент-серверного взаимодействия. Парсинг API.
Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного пользователя, сохранить JSON-вывод в файле *.json.

<p>
  <a href="https://github.com/YSamoy/Geekbrains_HW-data-parsing/blob/main/%D0%A3%D1%80%D0%BE%D0%BA_1_%D0%9E%D1%81%D0%BD%D0%BE%D0%B2%D1%8B_%D0%BA%D0%BB%D0%B8%D0%B5%D0%BD%D1%82_%D1%81%D0%B5%D1%80%D0%B2%D0%B5%D1%80%D0%BD%D0%BE%D0%B3%D0%BE_%D0%B2%D0%B7%D0%B0%D0%B8%D0%BC%D0%BE%D0%B4%D0%B5%D0%B9%D1%81%D1%82%D0%B2%D0%B8%D1%8F_%D0%A0%D0%B0%D0%B1%D0%BE%D1%82%D0%B0_%D1%81_API.ipynb">Решение</a>.
</p>

Урок 2. Парсинг данных HTML, DOM, XPath
Написать приложение и функцию, которые собирают основные новости с сайта на выбор lenta.ru, mail.ru . Для парсинга использовать XPath Структура данных должна содержать:
название источника, наименование новости, ссылку на новость, дата публикации

<p>
<a href="https://github.com/YSamoy/Geekbrains_HW-data-parsing/blob/main/%D0%A3%D1%80%D0%BE%D0%BA_2_%D0%9F%D0%B0%D1%80%D1%81%D0%B8%D0%BD%D0%B3_%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85_HTML%2C_DOM%2C_XPath_1.ipynb">Решение</a>
</p>

Урок 3. Парсинг данных Beautiful Soap
Написать приложение и функцию, которые собирают основные новости с сайта на выбор hh.ru, rabota.ru . Для парсинга использовать bs Структура данных должна содержать:
название источника, наименование вакансии, ссылку на нвакансию, дата публикации, заработная плата от, заработная плата до, валюта, работодатель

<p>
<a href="https://github.com/YSamoy/Geekbrains_HW-data-parsing/blob/main/%D0%A3%D1%80%D0%BE%D0%BA_3_%D0%9F%D0%B0%D1%80%D1%81%D0%B8%D0%BD%D0%B3_%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85_HTML%2C_Beautiful_Soap(rabota_ru).ipynb">Решение</a>
</p>

Урок 4. Система управления базами данных MongoDB в Python
Написать приложение, которое собирает основные новости с сайтов news.mail.ru, lenta.ru, yandex-новости. Для парсинга использовать XPath. Структура данных должна содержать:
Развернуть у себя на компьютере/виртуальной машине/хостинге MongoDB и реализовать функцию, записывающую собранные вакансии в созданную БД.
Написать функцию, которая будет добавлять в вашу базу данных только новые вакансии с сайта.

<p>
<a href="https://github.com/YSamoy/Geekbrains_HW-data-parsing/blob/main/%D0%A3%D1%80%D0%BE%D0%BA_4_%D0%A1%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0_%D1%83%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F_%D0%B1%D0%B0%D0%B7%D0%B0%D0%BC%D0%B8_%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85_MongoDB_%D0%B2_Python.ipynb">Решение</a>
</p>

Урок 5. Scrapy 1
Написать программу,по аналогии с проектом по парсингу вакансий с сайта rabota.ru и складывал все записи в БД (любую)

<p>
<a href="https://github.com/YSamoy/Geekbrains_HW-data-parsing/blob/main/rabota_ru.py">Решение</a>
<a href="https://github.com/YSamoy/Geekbrains_HW-data-parsing/blob/main/5_%D0%9F%D0%B0%D1%80%D1%81%D0%B8%D0%BD%D0%B3_%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85_Scrapy_%D0%9D%D0%B0%D1%87%D0%B0%D0%BB%D0%BE.ipynb">Проект</a>
</p>

Урок 6. Scrapy 2
Спарсить информацию с сайта castorama.ru и сложить данные в любую базу данных

<p>
<a href="https://github.com/YSamoy/Geekbrains_HW-data-parsing/blob/main/6.%20%D0%A4%D1%80%D0%B5%D0%B9%D0%BC%D0%B2%D0%BE%D1%80%D0%BA%20Scrapy%2C%20pipelines%2C%20Splash%20(castorama_parser).zip">Проект</a>
</p>

Урок 7. Парсинг данных в Selenium
Написать программу,которая будет собирать все входящие письма в в почтовый ящик. Структура должна содержать имя отправителя, тему письма, текст и дату отправки. Сложить данные в базу данных
<p>
<a href="https://github.com/YSamoy/Geekbrains_HW-data-parsing/blob/main/lesson_7_%D0%9F%D0%B0%D1%80%D1%81%D0%B8%D0%BD%D0%B3_%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85_Selenium_%D0%B2_Python.zip">Проект</a>
<a href="https://github.com/YSamoy/Geekbrains_HW-data-parsing/blob/main/7_%D0%9F%D0%B0%D1%80%D1%81%D0%B8%D0%BD%D0%B3_%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85_Selenium_%D0%B2_Python.ipynb">Решение</a>
</p>


![parse](https://user-images.githubusercontent.com/102718506/223711568-706b0b59-498d-4d6f-932c-a9e0f03ba216.jpg)
