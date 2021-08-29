## Новая схема БД SQL 

![](https://github.com/Iusar/SQL_3/blob/main/21.08.2021_database_diagram_%233.png)


## Задание 2. Команды SQL которые были использованы для создания БД по заданию 2.

```sql
CREATE TABLE IF NOT EXISTS Исполнители (
	id_artist SERIAL PRIMARY key,
	Имя VARCHAR(50) NOT NULL unique,
	id_genre INTEGER NOT NULL unique
);
CREATE TABLE IF NOT EXISTS Альбомы (
	id_album SERIAL PRIMARY key,
	Название_альбома VARCHAR(100)  NOT NULL, 
	Год_выпуска VARCHAR(4) NOT NULL,
	id_artist INTEGER REFERENCES Исполнители(id_artist) NOT NULL
);
CREATE TABLE IF NOT EXISTS Треки (
	id_track SERIAL PRIMARY key,
	Название_трека VARCHAR(100)  NOT NULL,
	Длительность VARCHAR(10) NOT NULL,
	id_album INTEGER REFERENCES Альбомы(id_album) NOT NULL
);
CREATE TABLE IF NOT EXISTS Жанры (
	id_genre SERIAL PRIMARY key,
	Название_жанра VARCHAR(100)  NOT NULL UNIQUE
);
ALTER TABLE Исполнители ADD CONSTRAINT id_genre FOREIGN KEY (id_genre) REFERENCES Жанры(id_genre);
```
## Задание 3. Команды SQL для изменения БД.

```sql
ALTER TABLE Исполнители DROP COLUMN id_genre;

CREATE TABLE IF NOT EXISTS Жанры_Исполнители (
	id_genre INTEGER REFERENCES Жанры(id_genre) NOT null,
	id_artist INTEGER REFERENCES Исполнители(id_artist) NOT null
);	
CREATE TABLE IF NOT EXISTS Альбомы_Исполнители (
	id_album INTEGER REFERENCES Альбомы(id_album) NOT null,
	id_artist INTEGER REFERENCES Исполнители(id_artist) NOT null
);	
CREATE TABLE IF NOT EXISTS Сборники (
	id_collection SERIAL PRIMARY key,
	Название_сборника VARCHAR(100)  NOT NULL, 
	Год_выпуска VARCHAR(4) NOT NULL,
	id_track INTEGER REFERENCES Треки(id_track) NOT NULL
);
CREATE TABLE IF NOT EXISTS Сборники_Треки (
	id_collection INTEGER REFERENCES Сборники(id_collection) NOT null,
	id_track INTEGER REFERENCES Треки(id_track) NOT null
);	
```
## Задание 4. Наполнение БД

## Исправление ошибок прошлых заданий. были не верные типы данных.  Из-за этих экспериментов я завалил сроки по заданию.

```sql
ALTER TABLE Альбомы ALTER COLUMN Год_выпуска type INTEGER USING "Год_выпуска"::INTEGER;
ALTER TABLE Сборники ALTER COLUMN Год_выпуска type INTEGER USING "Год_выпуска"::INTEGER;
ALTER TABLE Треки ALTER COLUMN Длительность type time USING "Длительность"::time;
```