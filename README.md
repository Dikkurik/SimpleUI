# Приложения "Птицы"

Небольшое приложение "Птицы" сделанное с помощью платформы SimpleUI, Python и json-файла в качестве NoSQL базы данных.

Для запуска необходимо запустить ui-файл BirdsApp.ui через андроид приложение SimpleUI.

# Функции приложения
- Приложения может выводить список и изображение птиц, хранящихся в БД. Для отображения птиц нужно нажать на кнопку "Птицы" в главном меню.

- Приложения может вносить название, описание (цвет перьев, например) и изображение птиц из галереи или фотокамеры устройства. 

>Для успешного запуска программы нужно расположить БД с птицами в папку файлов приложения SimpleUI на устройстве (путь для андроид: */storage/emulated/0/Android/data/ru.travelfood.simple_ui/files/*) и изображения в папку **/images** в папке файлов приложения

# Структура БД

Приложение считывает данные из json файла с названием db.json и имеет внутри структуру: <br /> {'имя_массива'
            <br />{[{
            <br />'name':'имя', 
            <br />'desc':'описание', 
            <br />'image':'путь_до _файла', 
            <br />'status':'булево_состояние'} 
            <br />
            <br />... 
            <br />
            <br />{**следущий элемент**}]}}





