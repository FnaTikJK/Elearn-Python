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


Разделённые CSV-файлы

[2007.csv](https://github.com/FnaTikJK/Elearn-Python/files/10199206/2007.csv)
[2008.csv](https://github.com/FnaTikJK/Elearn-Python/files/10199207/2008.csv)
[2009.csv](https://github.com/FnaTikJK/Elearn-Python/files/10199208/2009.csv)
[2010.csv](https://github.com/FnaTikJK/Elearn-Python/files/10199210/2010.csv)
[2011.csv](https://github.com/FnaTikJK/Elearn-Python/files/10199211/2011.csv)
[2012.csv](https://github.com/FnaTikJK/Elearn-Python/files/10199212/2012.csv)
[2013.csv](https://github.com/FnaTikJK/Elearn-Python/files/10199213/2013.csv)
[2014.csv](https://github.com/FnaTikJK/Elearn-Python/files/10199214/2014.csv)
[2015.csv](https://github.com/FnaTikJK/Elearn-Python/files/10199215/2015.csv)
[2016.csv](https://github.com/FnaTikJK/Elearn-Python/files/10199217/2016.csv)
[2017.csv](https://github.com/FnaTikJK/Elearn-Python/files/10199218/2017.csv)
[2018.csv](https://github.com/FnaTikJK/Elearn-Python/files/10199219/2018.csv)
[2019.csv](https://github.com/FnaTikJK/Elearn-Python/files/10199220/2019.csv)
[2020.csv](https://github.com/FnaTikJK/Elearn-Python/files/10199223/2020.csv)
[2021.csv](https://github.com/FnaTikJK/Elearn-Python/files/10199225/2021.csv)
[2022.csv](https://github.com/FnaTikJK/Elearn-Python/files/10199226/2022.csv)


# Многопроцессорность
До

![image](https://user-images.githubusercontent.com/70794890/209063870-b8bf4d59-debb-4a46-b904-a28beaee338e.png)

После 

![image](https://user-images.githubusercontent.com/70794890/209063920-291810c9-3348-44d9-8bc5-88bfc2c5b058.png)


# Concurrent futures
Без многопроцессорности

![image](https://user-images.githubusercontent.com/70794890/209063870-b8bf4d59-debb-4a46-b904-a28beaee338e.png)

Multiprocessing 

![image](https://user-images.githubusercontent.com/70794890/209063920-291810c9-3348-44d9-8bc5-88bfc2c5b058.png)

Concurrent futures

![image](https://user-images.githubusercontent.com/70794890/209064574-a6d3dc5e-bbe9-46ba-b182-d2e47aeb5204.png)

Concurrent futures сработал хуже multiproc => оставил решение с multiproc
