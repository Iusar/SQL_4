import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

db = 'postgresql://iusar:bVSFSuX6@localhost:5432/musicstore'

engine = sqlalchemy.create_engine(db)
connection = engine.connect()

# Очистка базы
connection.execute("""TRUNCATE Исполнители CASCADE;""")
connection.execute("""TRUNCATE Жанры CASCADE;""")
connection.execute("""TRUNCATE Альбомы CASCADE;""")
connection.execute("""TRUNCATE Треки CASCADE;""")
connection.execute("""TRUNCATE Сборники CASCADE;""")
connection.execute("""TRUNCATE Альбомы_Исполнители CASCADE;""")
connection.execute("""TRUNCATE Жанры_Исполнители CASCADE;""")
connection.execute("""TRUNCATE Сборники_Треки CASCADE;""")

# Создаем исполнителей в базу

connection.execute("""INSERT INTO Исполнители(id_artist, Имя) VALUES(1,'Guns & Roses');""")
connection.execute("""INSERT INTO Исполнители(id_artist, Имя) VALUES(2,'Cinderella');""")
connection.execute("""INSERT INTO Исполнители(id_artist, Имя) VALUES(3,'Bon Jovi');""")
connection.execute("""INSERT INTO Исполнители(id_artist, Имя) VALUES(4,'Jakyl');""")
connection.execute("""INSERT INTO Исполнители(id_artist, Имя) VALUES(5,'Midnight Memories');""")
connection.execute("""INSERT INTO Исполнители(id_artist, Имя) VALUES(6,'Tori Amos');""")
connection.execute("""INSERT INTO Исполнители(id_artist, Имя) VALUES(7,'Adele');""")
connection.execute("""INSERT INTO Исполнители(id_artist, Имя) VALUES(8,'The Cinematic Orchestra');""")

# Создаем жанры (сори я в них не разбираюсь)

connection.execute("""INSERT INTO Жанры(id_genre, Название_жанра) VALUES(1,'жанр_1');""")
connection.execute("""INSERT INTO Жанры(id_genre, Название_жанра) VALUES(2,'жанр_2');""")
connection.execute("""INSERT INTO Жанры(id_genre, Название_жанра) VALUES(3,'жанр_3');""")
connection.execute("""INSERT INTO Жанры(id_genre, Название_жанра) VALUES(4,'жанр_4');""")
connection.execute("""INSERT INTO Жанры(id_genre, Название_жанра) VALUES(5,'жанр_5');""")

# Создаем Альбомы

connection.execute("""INSERT INTO Альбомы(id_album, Название_альбома, Год_выпуска) VALUES(1,'Appetite for Destruction','1987');""")
connection.execute("""INSERT INTO Альбомы(id_album, Название_альбома, Год_выпуска) VALUES(2,'Use Your Illusion I','1991');""")
connection.execute("""INSERT INTO Альбомы(id_album, Название_альбома, Год_выпуска) VALUES(3,'Chinese Democracy','2008');""")
connection.execute("""INSERT INTO Альбомы(id_album, Название_альбома, Год_выпуска) VALUES(4,'Long Cold Winter','1988');""")
connection.execute("""INSERT INTO Альбомы(id_album, Название_альбома, Год_выпуска) VALUES(5,'Slippery When Wet','1986');""")
connection.execute("""INSERT INTO Альбомы(id_album, Название_альбома, Год_выпуска) VALUES(6,'Jackyl','1992');""")
connection.execute("""INSERT INTO Альбомы(id_album, Название_альбома, Год_выпуска) VALUES(7,'Take Me Home','2012');""")
connection.execute("""INSERT INTO Альбомы(id_album, Название_альбома, Год_выпуска) VALUES(8,'21','2018');""")
connection.execute("""INSERT INTO Альбомы(id_album, Название_альбома, Год_выпуска) VALUES(9,'Ma Fleur','2007');""")

# Создаем Треки

connection.execute("""INSERT INTO Треки(id_track, Название_трека, Длительность, id_album) VALUES(1,'My Michelle','00:05:57',1);""")
connection.execute("""INSERT INTO Треки(id_track, Название_трека, Длительность, id_album) VALUES(2,'Paradise City','00:05:37',1);""")
connection.execute("""INSERT INTO Треки(id_track, Название_трека, Длительность, id_album) VALUES(3,'Dont Cry','00:04:17',2);""")
connection.execute("""INSERT INTO Треки(id_track, Название_трека, Длительность, id_album) VALUES(4,'November Rain','00:03:45',2);""")
connection.execute("""INSERT INTO Треки(id_track, Название_трека, Длительность, id_album) VALUES(5,'Chinese Democracy','00:06:19',3);""")
connection.execute("""INSERT INTO Треки(id_track, Название_трека, Длительность, id_album) VALUES(6,'If You Dont Like It','00:05:35',4);""")
connection.execute("""INSERT INTO Треки(id_track, Название_трека, Длительность, id_album) VALUES(7,'Second Wind','00:05:35',4);""")
connection.execute("""INSERT INTO Треки(id_track, Название_трека, Длительность, id_album) VALUES(8,'Never Say Goodbye','00:03:21',5);""")
connection.execute("""INSERT INTO Треки(id_track, Название_трека, Длительность, id_album) VALUES(9,'Without Love','00:04:55',5);""")
connection.execute("""INSERT INTO Треки(id_track, Название_трека, Длительность, id_album) VALUES(10,'Jackyl','00:05:48',6);""")
connection.execute("""INSERT INTO Треки(id_track, Название_трека, Длительность, id_album) VALUES(11,'Push Comes to Shove','00:02:18',6);""")
connection.execute("""INSERT INTO Треки(id_track, Название_трека, Длительность, id_album) VALUES(12,'One Direction','00:03:02',7);""")
connection.execute("""INSERT INTO Треки(id_track, Название_трека, Длительность, id_album) VALUES(13,'Rolling in the Deep','00:04:17',8);""")
connection.execute("""INSERT INTO Треки(id_track, Название_трека, Длительность, id_album) VALUES(14,'Someone Like You','00:05:27',8);""")
connection.execute("""INSERT INTO Треки(id_track, Название_трека, Длительность, id_album) VALUES(15,'To Build a Home','00:06:32',9);""")
connection.execute("""INSERT INTO Треки(id_track, Название_трека, Длительность, id_album) VALUES(16,'Ma Fleur','00:03:11',9);""")
connection.execute("""INSERT INTO Треки(id_track, Название_трека, Длительность, id_album) VALUES(17,'Breathe','00:04:31',9);""")

# Создаем Сборники

connection.execute("""INSERT INTO Сборники(id_collection, Название_сборника, Год_выпуска) VALUES(1,'Сборник_1','2016');""")
connection.execute("""INSERT INTO Сборники(id_collection, Название_сборника, Год_выпуска) VALUES(2,'Сборник_2','2019');""")
connection.execute("""INSERT INTO Сборники(id_collection, Название_сборника, Год_выпуска) VALUES(3,'Сборник_3','2020');""")
connection.execute("""INSERT INTO Сборники(id_collection, Название_сборника, Год_выпуска) VALUES(4,'Сборник_4','2012');""")
connection.execute("""INSERT INTO Сборники(id_collection, Название_сборника, Год_выпуска) VALUES(5,'Сборник_5','2006');""")
connection.execute("""INSERT INTO Сборники(id_collection, Название_сборника, Год_выпуска) VALUES(6,'Сборник_6','2001');""")
connection.execute("""INSERT INTO Сборники(id_collection, Название_сборника, Год_выпуска) VALUES(7,'Сборник_7','2005');""")
connection.execute("""INSERT INTO Сборники(id_collection, Название_сборника, Год_выпуска) VALUES(8,'Сборник_8','2015');""")

# Наполняем Альбомы

connection.execute("""INSERT INTO Альбомы_Исполнители(id_album, id_artist) VALUES(1, 1);""")
connection.execute("""INSERT INTO Альбомы_Исполнители(id_album, id_artist) VALUES(2, 1);""")
connection.execute("""INSERT INTO Альбомы_Исполнители(id_album, id_artist) VALUES(3, 1);""")
connection.execute("""INSERT INTO Альбомы_Исполнители(id_album, id_artist) VALUES(4, 2);""")
connection.execute("""INSERT INTO Альбомы_Исполнители(id_album, id_artist) VALUES(5, 3);""")
connection.execute("""INSERT INTO Альбомы_Исполнители(id_album, id_artist) VALUES(6, 4);""")
connection.execute("""INSERT INTO Альбомы_Исполнители(id_album, id_artist) VALUES(7, 6);""")
connection.execute("""INSERT INTO Альбомы_Исполнители(id_album, id_artist) VALUES(8, 7);""")
connection.execute("""INSERT INTO Альбомы_Исполнители(id_album, id_artist) VALUES(9, 8);""")

# Наполняем Жанры

connection.execute("""INSERT INTO Жанры_Исполнители(id_genre, id_artist) VALUES(1,1);""")
connection.execute("""INSERT INTO Жанры_Исполнители(id_genre, id_artist) VALUES(1,2);""")
connection.execute("""INSERT INTO Жанры_Исполнители(id_genre, id_artist) VALUES(1,3);""")
connection.execute("""INSERT INTO Жанры_Исполнители(id_genre, id_artist) VALUES(1,8);""")
connection.execute("""INSERT INTO Жанры_Исполнители(id_genre, id_artist) VALUES(1,5);""")

connection.execute("""INSERT INTO Жанры_Исполнители(id_genre, id_artist) VALUES(2,3);""")
connection.execute("""INSERT INTO Жанры_Исполнители(id_genre, id_artist) VALUES(2,6);""")
connection.execute("""INSERT INTO Жанры_Исполнители(id_genre, id_artist) VALUES(2,7);""")
connection.execute("""INSERT INTO Жанры_Исполнители(id_genre, id_artist) VALUES(2,8);""")

connection.execute("""INSERT INTO Жанры_Исполнители(id_genre, id_artist) VALUES(3,1);""")
connection.execute("""INSERT INTO Жанры_Исполнители(id_genre, id_artist) VALUES(3,3);""")
connection.execute("""INSERT INTO Жанры_Исполнители(id_genre, id_artist) VALUES(3,8);""")

connection.execute("""INSERT INTO Жанры_Исполнители(id_genre, id_artist) VALUES(4,2);""")
connection.execute("""INSERT INTO Жанры_Исполнители(id_genre, id_artist) VALUES(4,4);""")
connection.execute("""INSERT INTO Жанры_Исполнители(id_genre, id_artist) VALUES(4,5);""")
connection.execute("""INSERT INTO Жанры_Исполнители(id_genre, id_artist) VALUES(4,6);""")

connection.execute("""INSERT INTO Жанры_Исполнители(id_genre, id_artist) VALUES(5,1);""")
connection.execute("""INSERT INTO Жанры_Исполнители(id_genre, id_artist) VALUES(5,2);""")
connection.execute("""INSERT INTO Жанры_Исполнители(id_genre, id_artist) VALUES(5,3);""")
connection.execute("""INSERT INTO Жанры_Исполнители(id_genre, id_artist) VALUES(5,6);""")

# Наполняем Сборники

connection.execute("""INSERT INTO Сборники_Треки(id_collection, id_track) VALUES(1,1);""")
connection.execute("""INSERT INTO Сборники_Треки(id_collection, id_track) VALUES(1,2);""")
connection.execute("""INSERT INTO Сборники_Треки(id_collection, id_track) VALUES(1,3);""")
connection.execute("""INSERT INTO Сборники_Треки(id_collection, id_track) VALUES(1,4);""")
connection.execute("""INSERT INTO Сборники_Треки(id_collection, id_track) VALUES(1,5);""")
connection.execute("""INSERT INTO Сборники_Треки(id_collection, id_track) VALUES(1,8);""")
connection.execute("""INSERT INTO Сборники_Треки(id_collection, id_track) VALUES(1,10);""")
connection.execute("""INSERT INTO Сборники_Треки(id_collection, id_track) VALUES(1,11);""")
connection.execute("""INSERT INTO Сборники_Треки(id_collection, id_track) VALUES(1,15);""")

connection.execute("""INSERT INTO Сборники_Треки(id_collection, id_track) VALUES(2,1);""")
connection.execute("""INSERT INTO Сборники_Треки(id_collection, id_track) VALUES(2,2);""")
connection.execute("""INSERT INTO Сборники_Треки(id_collection, id_track) VALUES(2,6);""")
connection.execute("""INSERT INTO Сборники_Треки(id_collection, id_track) VALUES(2,7);""")
connection.execute("""INSERT INTO Сборники_Треки(id_collection, id_track) VALUES(2,8);""")
connection.execute("""INSERT INTO Сборники_Треки(id_collection, id_track) VALUES(2,10);""")
connection.execute("""INSERT INTO Сборники_Треки(id_collection, id_track) VALUES(2,11);""")
connection.execute("""INSERT INTO Сборники_Треки(id_collection, id_track) VALUES(2,16);""")
connection.execute("""INSERT INTO Сборники_Треки(id_collection, id_track) VALUES(2,17);""")

connection.execute("""INSERT INTO Сборники_Треки(id_collection, id_track) VALUES(3,1);""")
connection.execute("""INSERT INTO Сборники_Треки(id_collection, id_track) VALUES(3,5);""")
connection.execute("""INSERT INTO Сборники_Треки(id_collection, id_track) VALUES(3,7);""")
connection.execute("""INSERT INTO Сборники_Треки(id_collection, id_track) VALUES(3,8);""")
connection.execute("""INSERT INTO Сборники_Треки(id_collection, id_track) VALUES(3,9);""")
connection.execute("""INSERT INTO Сборники_Треки(id_collection, id_track) VALUES(3,13);""")
connection.execute("""INSERT INTO Сборники_Треки(id_collection, id_track) VALUES(3,14);""")
connection.execute("""INSERT INTO Сборники_Треки(id_collection, id_track) VALUES(3,15);""")
connection.execute("""INSERT INTO Сборники_Треки(id_collection, id_track) VALUES(3,16);""")
connection.execute("""INSERT INTO Сборники_Треки(id_collection, id_track) VALUES(3,17);""")
connection.execute("""INSERT INTO Сборники_Треки(id_collection, id_track) VALUES(3,17);""")



