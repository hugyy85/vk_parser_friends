# vk_parser_friends


Данный скрипт собирает информацию по друзьям друзей вконтакте определенного юзера. 
И создает текстовые файлы:


<b>contacts.txt</b> - все открытые контакты друзей(и друзей друзей)<br>
<b>country.txt</b> - инфо по количеству живущих друзей в разных странах<br>
<b>city.txt</b> - инфо по количеству живущих друзей в разных городах<br>
<b>names.txt</b> - инфо по количеству  одинаковых имен друзей<br>
<b>friends.txt</b> - общее количество друзей и их имена<br>



Можно получить информацию по количеству друзей в разных странах и городах.
Так же, есть возможность сделать большую выборку(по друзьям друзей). 

Для работы необходим MySQL или другая скульная база данных
Все тесты проводились на MySQL

	Зависимости:

	pip install -r requirements.txt
	
	Чтобы запустить:

	-Открываем окно команд в той папке куда сохранен скрипт
	-вводим python main.py



Чтобы выбрать юзера, необходимо поменять nickname в файле config.py

Так же там можно выбрать, как именно будет происходить выборка:
-
если big_database = 0, то выборка будет сформирована по всем друзьям выбраного юзера (в примере id11706070 около 260 друзей)

-если big_database = 1, то выборка будет сформирована по друзьям друзей выбранного юзера (более 27000 друзей) Это занимает более часа!!

И в этом же файле прописать настройки для подключения к базе данных (user, password, db_name, host)

			Алгоритм Работы:

1. Скрипт пытается подключиться к MySQL базе данных(которая создана до этого)<br>

2. Если таблицы ранее были созданы, они удаляются<br>

3. Создаются новые таблицы определенной структуры<br>

4. Проверка большая это выборка или нет<br>
	4.1 Если большая, то собирается информация по всем друзьям юзера и хранится в списке<br>
	4.2 Если маленькая то в список записывается только сам юзер<br>

5. Идет перебор списка друзей сформированного ранее<br>
	5.1 Далее происходит сбор информации по друзьям итерируемого друга<br>
	5.2 Начинается парсинг получаенной информации<br>
		5.2.1 Запись полученой инорфмации в таблицы<br>
