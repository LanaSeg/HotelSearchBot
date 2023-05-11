# Too Easy Travel BOT

## Описание бота

Телеграм бот, с помощью которого можно получать информацию об отелях, расположенных по всему миру.

Используемая платформа: **[Hotels.com](https://hotels.com/).**

Попробуйте воспользоваться ботом: [**HotelSearchBot**](https://t.me/SS_HotelSearchBot)

![1.jpg](media/1.jpg?t=1682006625366)

## Основные технологии и библиотеки

Для разработки и функционирования проекта используется открытый API Hotels, который расположен на сайте **[rapidapi.com](https://rapidapi.com/apidojo/api/hotels4/).**

* Python (3.10);
* pyTelegramBotAPI;
* requests;
* telebot.

## Установка на локальном сервере:

1. Скопируйте все содержимое репозитория в отдельныйкаталог.
2. Установите все библиотеки. Вы можете использовать команду:

   `pip install -r requirements.txt`
3. Запустите файл [main.py](main.py).

## Возможности бота

#### Команды бота:

`/start` - запуск бота

![start_img.jpg](media/start_img.jpg?t=1682005662326)

> [Смотреть запуск команды /start](https://gitlab.skillbox.ru/lana_seg/PA_Python_DPO_bot/-/raw/homework/project/media/start.GIF)

#### Кнопки бота:

`help` - список кнопок и их описание

`lowprice` - поиск дешевых отелей

`highprice` - поиск дорогих отелей

`bestdeal` - поиск лучших предложений

`history` - история поиска

![btn.jpg](media/btn.jpg?t=1682005710465)

##### Кнопка lowprice

После нажатия на кнопку у пользователя запрашивается:

1. Город, где будет проводиться поиск.
2. Количество отелей, которые необходимо вывести в результате (не больше 10).
3. Необходимость загрузки и вывода фотографий для каждого отеля (“Да/Нет”)

a. При положительном ответе пользователь также вводит количество необходимых фотографий (не больше 5)

> [Смотреть работу кнопки lowprice](https://gitlab.skillbox.ru/lana_seg/PA_Python_DPO_bot/-/raw/homework/project/media/lowprice.GIF)

##### Кнопка highprice

После нажатия на кнопку у пользователя запрашивается:

1. Город, где будет проводиться поиск.
2. Количество отелей, которые необходимо вывести в результате (не больше 10).
3. Необходимость загрузки и вывода фотографий для каждого отеля (“Да/Нет”)

a. При положительном ответе пользователь также вводит количество необходимых фотографий (не больше 5)

> [Смотреть работу кнопки highprice](https://gitlab.skillbox.ru/lana_seg/PA_Python_DPO_bot/-/raw/homework/project/media/highprice.GIF)

##### Кнопка bestdeal

После нажатия на кнопку у пользователя запрашивается:

1. Город, где будет проводиться поиск.
2. Диапазон цен.
3. Диапазон расстояния, на котором находится отель от центра.
4. Количество отелей, которые необходимо вывести в результате (не больше 10).
5. Необходимость загрузки и вывода фотографий для каждого отеля (“Да/Нет”)

a. При положительном ответе пользователь также вводит количество необходимых фотографий (не больше 5)

> [Смотреть работу кнопки bestdeal](https://gitlab.skillbox.ru/lana_seg/PA_Python_DPO_bot/-/raw/homework/project/media/highprice.GIF)

##### Кнопка history

После нажатия на кнопку пользователю выводится история поиска отелей. Сама история содержит:

1. Кнопку, которую выбрал пользователь.
2. Дату и время ввода.
3. Отели, которые были найдены.

> [Смотреть работу кнопки history](https://gitlab.skillbox.ru/lana_seg/PA_Python_DPO_bot/-/raw/homework/project/media/history.GIF)

##### Кнопка help

Подробнее рассказывает о каждой кнопке

![help.jpg](media/help.jpg?t=1682005828777)