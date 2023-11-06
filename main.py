################################
#я просто решил копировать и вставить с презентации в место прописания внунтри класса принта
################################################

##################################################
#111111111111111111111111111111111111111111111111#
##################################################

import random


# class MusicAlbum:
#     def __init__(self, title, artist, release_year, genre, tracklist):
#         self.title=title
#         self.artist=artist
#         self.release_year=release_year
#         self.genre=genre
#         self.tracklist=tracklist
#
#
#     def play_random_track(self):
#         rand=random.randint(1,len(self.tracklist))
#         print(rand, self.tracklist[rand-1] )
#
# album4 = MusicAlbum("Deutschland", "Rammstein", 2019, "Neue Deutsche Härte",
#                     ["Deutschland", "Radio", "Zeig dich", "Ausländer", "Sex",
#                      "Puppe", "Was ich liebe", "Diamant", "Weit weg", "Tattoo",
#                      "Hallomann"])
# print("Название:", album4.title)
# print("Исполнитель:", album4.artist)
# print("Год:", album4.release_year)
# print("Жанр:", album4.genre)
# print("Треки:", album4.tracklist)
# album4.play_random_track()


#####################################
#22222222222222222222222222222222222#
#####################################

# class Student:
#     def __init__(self,name, age, grade, scores):
#         self.name=name
#         self.age=age
#         self.grade=grade
#         self.scores=scores
#
#     def average_score(self):
#         return sum(self.scores)/len(self.scores)
#
# student2 = Student("Егор Данилов", 12, "5B", [5, 4, 4, 5])
# print("Имя:", student2.name)
# print("Возраст:", student2.age)
# print("Класс:", student2.grade)
# print("Оценки:", *student2.scores)
# print("Средний балл:", student2.average_score())


########################################
#33333333333333333333333333333333333333#
########################################


# class Recipe:
#     def __init__(self,name, recipe):
#         self.name=name
#         self.recipe=recipe
#
#     def print_ingredients(self):
#         print('Ингредиенты для ', self.name)
#         for item in self.recipe:
#             print(item)
#
#     def cook(self):
#         print(f'\nСегодня мы готовим {self.name}.\nВыполняем инструкцию по приготовлению блюда{self.name}...\nБлюдо {self.name} готово!\n\n')
#
# # создаем рецепт спагетти болоньезе
# spaghetti = Recipe("Спагетти болоньезе", ["Спагетти", "Фарш", "Томатный соус", "Лук", "Чеснок", "Соль"])
#
# # печатаем список продуктов для рецепта спагетти
# spaghetti.print_ingredients()
#
# # готовим спагетти
# spaghetti.cook()
#
# # создаем рецепт для кекса
# cake = Recipe("Кекс", ["Мука", "Яйца", "Молоко", "Сахар", "Сливочное масло", "Соль", "Ванилин"])
#
# # печатаем рецепт кекса
# cake.print_ingredients()
#
# # готовим кекс
# cake.cook()

##########################################
#4444444444444444444444444444444444444444#
##########################################

# class Publisher:
#     def __init__(self,name,location):
#         self.name=name
#         self.location=location
#
#     def get_info(self):
#         return f'{self.name} ({self.location})'
#
#     def publish(self, message):
#         print(f'Готовим \"{message}\" к публикации {self.get_info()}')
#
# class BookPublisher(Publisher):
#     def __init__(self,name,location,num_author):
#         super().__init__(name, location)
#         self.num_author=num_author
#
#     def publish(self, message, author):
#         print(f'Передаем рукопись \'{message}\', написанную автором {author} в издательстве {self.get_info()}')
#
#     def num_authors(self):
#         print(f'количество авторов в \"{self.name}\" состовляет {self.num_author}')
#
# class NewspaperPublisher(Publisher):
#     def __init__(self,name,location,num_pag):
#         super().__init__(name, location)
#         self.num_pag=num_pag
#
#     def publish(self, message):
#         print(f'Печатаем свежий номер со статьей \"{message}\" на главной странице в издательстве {self.get_info()}')
#
#     def num_pages(self):
#         print(f'количество страниц: {self.num_pag}')
#
#
# publisher = Publisher("АБВГД Пресс", "Москва")
# publisher.publish("Справочник писателя")
#
# book_publisher = BookPublisher("Важные Книги", "Самара", 52)
# book_publisher.publish("Приключения Чебурашки", "В.И.Пупкин")
# book_publisher.num_authors()
#
# newspaper_publisher = NewspaperPublisher("Московские вести", "Москва", 12)
# newspaper_publisher.publish("Новая версия Midjourney будет платной")
# newspaper_publisher.num_pages()


##############################
#5555555555555555555555555555#
##############################

# class BankAccount:
#     def __init__(self,balance,interest_rate):
#         self.__balance=balance
#         self.__interest_rate=interest_rate
#         self.__transactions=[]
#
#
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             self.__transactions.append(f"Внесение наличных на счет: {amount}")
#         else:
#             return "депозит не может быть меньше 0"
#
#     def withdraw(self, amount):
#         if amount > 0 and amount <= self.__balance:
#             self.__balance -= amount
#             self.__transactions.append(f"Снятие наличных: {amount}")
#         else:
#             return 'Нельзя отнять  меньше чем 0 и больше чем баланс'
#
#     def add_interest(self):
#         interest_amount = self.__balance * self.__interest_rate
#         self.__balance += interest_amount
#         self.__transactions.append(f"Добавлены проценты  ({self.__interest_rate}), что состовляет {interest_amount}")
#
#     def history(self):
#         for transaction in self.__transactions:
#             print(transaction)
#
#
# # создаем объект счета с балансом 100000 и процентом по вкладу 0.05
# account = BankAccount(100000, 0.05)
#
# # вносим 15 тысяч на счет
# account.deposit(15000)
#
# # снимаем 7500 рублей
# account.withdraw(7500)
#
# # начисляем проценты по вкладу
# account.add_interest()
#
# # печатаем историю
# account.history()



##########################################
#6666666666666666666666666666666666666666#
##########################################


# class Employee:
#     def __init__(self,name,age,salary):
#         self.__name=name
#         self.__age=age
#         self.__salary=salary
#         self.__bonus=0
#
#     def get_name(self):
#         return self.__name
#
#     def get_age(self):
#         return self.__age
#
#     def get_salary(self):
#         return self.__salary
#
#     def set_bonus(self, bonus):
#         self.__bonus=bonus
#
#     def get_bonus(self):
#         return self.__bonus
#
#     def get_total_salary(self):
#         return self.__salary+self.__bonus
#
# # создаем сотрудника с именем, возрастом и зарплатой
# employee = Employee("Марина Арефьева", 30, 90000)
#
# # устанавливаем бонус для сотрудника
# employee.set_bonus(15000)
#
# # выводим имя, возраст, зарплату, бонус и общую зарплату сотрудника
# print("Имя:", employee.get_name())
# print("Возраст:", employee.get_age())
# print("Зарплата:", employee.get_salary())
# print("Бонус:", employee.get_bonus())
# print("Итого начислено:", employee.get_total_salary())


#################################################
#77777777777777777777777777777777777777777777777#
#################################################


# class Animal:
#     def __init__(self, name, species, legs):
#         self.name = name
#         self.species = species
#         self.legs = legs
#
#     def voice(self):
#         print(self.name, "подает голос")
#
#     def move(self):
#         print(self.name, "дергает хвостом")
#
#
# class Dog(Animal):
#     def __init__(self, name, species, legs):
#         super().__init__(name, species, legs)
#         self.breed = species
#
#     def bark(self):
#         print(self.breed, self.name, "лает")
#
#
# class Bird(Animal):
#     def __init__(self, name, species, legs, wingspan):
#         super().__init__(name, species, legs)
#         self.wingspan = wingspan
#
#     def fly(self):
#         print(self.species, self.name, "летит")
#
#     def wingspans(self):
#         print(self.name, str('размахивает крыльями'))
#
#
# dog = Dog("Геральт", "доберман", 4)
# bird = Bird("Вася", "попугай", 2, "средний")
#
# dog.voice()
# bird.voice()
# dog.move()
# bird.move()
# dog.bark()
# bird.fly()
# bird.wingspans()


#############################
#888888888888888888888888888#
#############################

# class Shape:
#     def __init__(self, name='', color=''):
#         self.name=name
#         self.color=color
#
#     def describe(self):
#         print('\nЭто геометрическая фигура, цвет -', self.color)
#
#
# class Circle(Shape):
#     def __init__(self, color, radius, name='окружность'):
#         self.color=color
#         self.name=name
#         self.radius=radius
#
#     def describe(self):
#         super().describe()
#         print(f'это {self.name}. Радиус - {self.radius}см, цвет - {self.color}')
#
#
#     def area(self):
#         print('площадь этой окружности: ',3.14*(self.radius**2))
#
# class Rectangle(Shape):
#     def __init__(self, color, length,width, name='прямоугольник'):
#         self.color = color
#         self.name = name
#         self.length = length
#         self.width=width
#
#     def describe(self):
#         super().describe()
#         print(f'это {self.color} {self.name}. Длина - {self.length}см, высота - {self.width}см')
#
#     def area(self):
#         print('площадь этого прямоугольника: ', self.width*self.length)
#
# class Triangle(Shape):
#     def __init__(self, color, base,height, name='треугольник'):
#         self.color = color
#         self.name = name
#         self.base = base
#         self.height=height
#
#     def describe(self):
#         super().describe()
#         print(f'это {self.color} {self.name} с основанием - {self.base}см и высотой - {self.height}см')
#
#     def area(self):
#         print('площадь треугольника: ', (self.height*self.base)/2)
#
#
#
#
# circle = Circle("красный", 5)
# circle.describe()
# circle.area()
#
# rectangle = Rectangle("синий", 3, 4)
# rectangle.describe()
# rectangle.area()
#
# triangle = Triangle("фиолетовый", 6, 8)
# triangle.describe()
# triangle.area()


#############################
#099999999999999999999999999#
#############################

# class Candy:
#     def __init__(self,name,price,weight):
#         self.name=name
#         self.price=price
#         self.weight=weight
#
#
# class Chocolate(Candy):
#     def __init__(self,name,price,weight,cocoa_percentage,chocolate_type):
#         super().__init__(name, price, weight)
#         self.cocoa_percentage=cocoa_percentage
#         self.chocolate_type=chocolate_type
#
# class Gummy(Candy):
#     def __init__(self, name, price, weight,flavor,shape):
#         super().__init__(name, price, weight)
#         self.flavor=flavor
#         self.shape=shape
#
# class HardCandy(Candy):
#     def __init__(self, name, price, weight,flavor,filled):
#         super().__init__(name, price, weight)
#         self.flavor=flavor
#         self.filled=filled
#
#
# chocolate = Chocolate(name="Швейцарские луга", price=325.50, weight=220, cocoa_percentage=40, chocolate_type="молочный")
# gummy = Gummy(name="Жуй-жуй", price=76.50, weight=50, flavor="вишня", shape="медведь")
# hard_candy = HardCandy(name="Crazy Фрукт", price=35.50, weight=25, flavor="манго", filled=True)
# print("\nШоколадные конфеты:")
# print(f"Название конфет: {chocolate.name}")
# print(f"Стоимость: {chocolate.price} руб")
# print(f"Вес брутто: {chocolate.weight} г")
# print(f"Процент содержания какао: {chocolate.cocoa_percentage}")
# print(f"Тип шоколада: {chocolate.chocolate_type}")
# print("\nМармелад жевательный:")
# print(f"Название конфет: {gummy.name}")
# print(f"Стоимость: {gummy.price} руб")
# print(f"Вес брутто: {gummy.weight} г")
# print(f"Вкус: {gummy.flavor}")
# print(f"Форма: {gummy.shape}")
# print("\nФруктовые леденцы:")
# print(f"Название конфет: {hard_candy.name}")
# print(f"Стоимость: {hard_candy.price} руб")
# print(f"Вес брутто: {hard_candy.weight} г")
# print(f"Вкус: {hard_candy.flavor}")
# print(f"Начинка: {hard_candy.filled}")


########################################
#10#10#10#10#10#10#10#10#10#10#10#10#10#
########################################

# class Soldier:
#     def __init__(self,name ,rank,service_number ):
#         self.__name=name
#         self.rank=rank
#         self.__service_number=service_number
#         print(f'\nСоздан новый игровой персонаж типа Soldier с атрибутами: \nname: {name}, rank: {rank}, service number: {service_number}')
#         self.ranks=['рядовой','ефрейтор','младший сержант','сержант','старший сержант','старшина','прапорщик','старший прапорщик','лецтинант','капитан','генерал']
#         self.__halper_for_ranks=0
#
#     def ranks_info(self):
#         print('\nВот список всех рангов:')
#         for i in range (1, len(self.ranks)+1):
#             print(f'{i})', self.ranks[i-1])
#         print('через get_rank ты можешь сразу дать нужное звание персонажуб написав сразу номер звания\n')
#
#     def get_rank(self, rank_number):
#         print(f'Новое звание у {self.__name}. Теперь он {self.ranks[(rank_number-1)%11]}')
#         self.rank = self.ranks[rank_number-1]
#         self.__halper_for_ranks=rank_number-1
#
#     def promote(self):
#         print(f'{self.__name} повышен в звании. Теперь он {self.ranks[self.__halper_for_ranks+1]}')
#
#     def demote(self):
#         print(f'{self.__name} понижен в звании. Теперь он {self.ranks[self.__halper_for_ranks-1]}')
#
#     def check_service_number(self, checker):
#         if checker==self.__service_number:
#             print('\nДа, порядковый номер верный и он подтвержден')
#         else:
#             print('\nПорядковый номер не подтвержден.')
#
#
#
# soldier1 = Soldier("Иван Сусанин", "рядовой", 12345)
# soldier1.ranks_info()
# soldier1.get_rank(4)
# soldier1.promote()
# soldier1.demote()
# soldier1.check_service_number(12345)
# soldier1.check_service_number(12345325543)
# print('\n', soldier1.rank)




