# Интеграция Django с PostgreSQL для разработки веб-API и обмена данными 1С:Предприятия
По мере развития бизнеса возрастает потребность в интеграции различных программных систем для оптимизации операционной деятельности. Это исследование затрагивает успешное использование Django в сочетании с PostgreSQL для создания веб-API, которое обслуживает данные для платформы 1C:Предприятие — демонстрируя практическое сотрудничество между фреймворками веб-разработки и системами планирования ресурсов предприятия.
В современной среде веб-разработки и интеграции корпоративных систем все чаще возникает потребность в беспрепятственном взаимодействии и обмене данными между разнообразными платформами. Django — отличный фреймворк для веб-разработчиков построения мощных API благодаря своей простоте и надежности. Используя возможности Django вместе с PostgreSQL, продвинутой opensource базой данных, можно настроить надежный бэкенд для ваших приложений.
Сценарий интеграции обычно выглядит следующим образом:
1.	Данные генерируются и хранятся в PostgreSQL.
2.	Django извлекает данные из PostgreSQL, обрабатывает их, и через REST API предоставляет в структурированном формате JSON.
3.	1C периодически отправляет HTTP GET запросы на API-эндпоинт Django.
4.	После получения запроса Django извлекает и сериализует данные, возвращая ответ в формате JSON.
5.	1C получает этот ответ, десериализует JSON, и затем данные манипулируются или сохраняются в базе данных 1C по мере необходимости.




## Настройка разработки
Установка и настройка Django, создание базы данных PostgreSQL и подготовка подходящего окружения для разработки и тестирования. Убедитесь, что Python и pip (инсталлятор пакетов Python) уже установлены в системе Windows. Инсталляторы Python для Windows по умолчанию включают pip. Вот руководство по установке и настройке Django в сочетании с базой данных PostgreSQL и настройке подходящего окружения для разработки и тестирования в системе Windows:
1. Установите PostgreSQL:
•	Скачайте инсталлятор PostgreSQL для Windows по следующему адресу: https://www.postgresql.org/download/windows/ .
•	Запустите скачанный инсталлятор, в который обычно входят сервер PostgreSQL, pgAdmin — графический инструмент управления и разработки вашей базы данных, и Stack Builder — менеджер пакетов, который может быть использован для скачивания и установки дополнительных инструментов и драйверов PostgreSQL.
•	Во время установки задайте пароль для суперпользователя PostgreSQL (postgres) и запишите его. Также запомните номер порта, на котором будет работать PostgreSQL (по умолчанию это 5432).
•	После установки убедитесь, что вы можете подключиться к серверу баз данных PostgreSQL с помощью инструмента pgAdmin.

![pgAdmin](https://github.com/user-attachments/assets/45a1fc64-9626-4637-9385-eee1a6c97870)
Рис1. Инструмент pgAdmin.

2. Настройте базу данных PostgreSQL:
•	Запустите pgAdmin и подключитесь к экземпляру PostgreSQL, используя учетные данные, заданные во время установки.
•	Создайте новую базу данных StudentDB и таблицу StudentRegistration_student.

![Erd](https://github.com/user-attachments/assets/ce579b51-d7a1-493f-8016-e6e17f019a43)
![Erd2](https://github.com/user-attachments/assets/e1ed235a-67fd-4520-bcb4-d1581772c9af)

Рис2 . ERD для таблиц

3. Настройка среды Python:
•	Откройте командную строку или PowerShell от имени администратора.
•	Создайте каталог для проекта и перейдите в него:
mkdir student
cd student
•	Создайте виртуальную среду в каталоге вашего проекта:
python -m venv myenv
•	Активируйте виртуальную среду:
myenv\Scripts\activate

4. Установите Django и psycopg2:
•	Установите Django и psycopg2 (который является адаптером Python PostgreSQL ) в активированной виртуальной среде:
pip install django psycopg2

![install Django](https://github.com/user-attachments/assets/9d7392ab-2652-40c5-bcf2-369c60f62976)

Рисунок 3 – Установка Django и psycopg2.

5. Создайте новый проект Django и настройте PostgreSQL :
•	Создайте новый проект Django , выполнив:
django-admin startproject student_registration .
•	Откройте файл настроек Django ( myproject /settings.py), найдите параметр DATABASES и измените его на использование PostgreSQL.

![install databases in Jdango](https://github.com/user-attachments/assets/696ec70e-0d27-46a7-a09d-4a86765115ee)

Рис 4. Настройка БАЗ ДАННЫХ в Django.

•	Выполните первоначальную миграцию с помощью сценария Manage.py Django , чтобы подготовить базу данных PostgreSQL :
python manage.py migrate
•	Запустите сервер разработки Django с помощью следующей команды:
python manage.py runserver
•	Сервер разработки будет работать по адресу  http://127.20.10.1:8181/ (localhost on port 8181). можно открыть этот URL-адрес в веб-браузерах.
2.2 Проектирование и разработка API
Использование Django ORM (объектно-реляционное сопоставление) для взаимодействия с PostgreSQL и платформой REST Django для создания API, который выводит данные в формате JSON.
Две функции showFiltered () и show() являются частью Django . Эти функции служат конечными точками для API, предоставляя внешним клиентам механизмы для получения данных «Студент» в структурированном формате JSON с возможностью пометить данные как обработанные, если это необходимо. Функции извлекают записи Student, сериализуют их в JSON, сохраняют эти данные в файл JSON в каталоге Django .
1.	showFiltered : эта функция предназначена для ситуаций, когда вы хотите обработать и ответить только на подмножество записей учащихся, которые еще не были «отправлены». При вызове он получает эти записи, помечает их как «отправленные», сохраняет изменения в базе данных, записывает сериализованные данные в файл с отметкой времени для ведения учета и возвращает данные в виде ответа JSON.
2.	show: это функция более общего назначения, которая извлекает все записи Student в системе, сериализует их в JSON, сохраняет эти данные в файл с именем « output.json » (перезаписывая его, если он существует) и возвращает данные в виде JSON-ответ.

 ![showFiltered](https://github.com/user-attachments/assets/42ff6c78-cc04-4131-ae97-be97b6ecea27)

Рисунок 5 – функции showFiltered () и show()

 ![Api](https://github.com/user-attachments/assets/5bd418b0-3218-465d-8542-b3c759d0bf50)

Рис. 6. Проектирование и разработка API

# 1C:Enterprise интеграция
Установление связи между API Django и платформой 1C:Предприятие с использованием встроенных HTTP-функций для отправки и получения данных.
Это включает в себя несколько процедур, предназначенных для взаимодействия с сервером и обработки JSON-ответов, связанных с данными студентов.
1.	Директива &НаКлиенте указывает, что следующая процедура должна выполняться на стороне клиента, в то время как &НаСервере указывает на выполнение на сервере.
2.	Процедура Команда1 - это клиентская процедура, которая вызывает другую процедуру Команда1НаСервере, выполняющую серверную работу.
3.	Процедура Команда1НаСервере устанавливает HTTP-соединение с сервером и отправляет запрос к конечной точке “/show”. Она обрабатывает JSON-ответ, создает объекты для ‘StudentRegister_student’ из разобранного JSON и записывает эти данные в базу данных сервера.
4.	Процедура Команда2 на стороне клиента вызывает Команда1НаСервере2, которая похожа на Команда1НаСервере, но делает запрос к конечной точке “/showFiltered”. Она также содержит проверку для отображения сообщений в зависимости от доступности данных или результата действия.
5.	Процедура Команда3 вызывает Команда1НаСервере3, передавая путь к файлу в качестве аргумента. Она предназначена для чтения данных из определенного JSON-файла на сервере, их разбора и заполнения объектов ‘StudentRegister_student’ так же, как и в предыдущих процедурах.
6.	Процедура ВыбратьФайл - это клиентская процедура, позволяющая пользователям выбирать файл через диалоговое окно, что, вероятно, приводит к выбору JSON-файла для обработки сервером.
7.	Процедура ПослеВыбораФайла обрабатывает выбранный пользователем файл, извлекает его имя и вызывает Команда1НаСервере3 с именем файла для его обработки.

![1](https://github.com/user-attachments/assets/4a536278-9726-49bb-af86-c7a278bc220e)
Рис 7 Каталог IC:Interprice StudentRegistration_student
 
![2](https://github.com/user-attachments/assets/263a032c-996d-42a7-b29f-e6f547aca936)
Рис 8. Конфигурация добавления студента из HTTP-запроса и файла JSON.

 
![3](https://github.com/user-attachments/assets/5633ce3b-7473-4ee5-b9ca-ca023eee62cf)
Рисунок 8 Форма Списка StudentRegistration_student




# Заключение
Интеграция Django с PostgreSQL для разработки веб-API и платформой 1C:Предприятие демонстрирует успешное взаимодействие между фреймворком веб-разработки и программным обеспечением для управления предприятием.
