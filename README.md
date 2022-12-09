Тесты
![image](https://user-images.githubusercontent.com/70794890/206713711-121d2c8a-0347-416c-ad2a-4980c26f451d.png)

Профилирвание

1) Метод strptime показал следующие результаты

![2022-12-09_19-01-37](https://user-images.githubusercontent.com/70794890/206723122-f24d8a0a-0c67-45d9-8666-dab864fa6510.png)

2)Заменил на custom_parse_substr, получил следующее

![image](https://user-images.githubusercontent.com/70794890/206724562-1b0e4c31-19fa-4661-9172-8fdf408ee93a.png)


3)Заменил его на custom_parse, получил следующее время работы

![2022-12-09_19-20-08](https://user-images.githubusercontent.com/70794890/206723221-6661af00-3fde-4dee-b56a-29d31928dd09.png)

В итоге получил увеличение скорости в 5 раз
