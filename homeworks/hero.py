# 1)создать класс SuperHero
class SuperHero:  # родительский класс или суперкласс
    # свойство класса
    people = 'people'

    # конструктор класса - инициализатор
    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def printName(self):
        # метод, который выводит имя героя
        print(f'{self.name}')

    def helth_points2(self):
        # метод, который умножает здоровье героя на 2
        self.health_points = int(self.health_points) * 2

    def __str__(self):
        # метод, который
        # выводит прозвище героя, его суперспособность и его здоровье
        return f'{self.nickname}, {self.superpower}, {self.health_points}'

    def __len__(self):
        # метод, который считает длину коронной фразы героя
        return len(self.catchphrase)


geo_archon = SuperHero('Чжун Ли', 'Дед',
                       'Падение кометы', '50000',
                       'Османтусовое вино такое же, как я помню... '
                       'но где те, кто разделят воспоминания?')

print(geo_archon)
geo_archon.printName()
geo_archon.helth_points2()
print(geo_archon.health_points)
print(len(geo_archon))


# Наследование
# Создать 2 класса наследованных от класса SuperHero
class Air(SuperHero):
    fly = False

    def __init__(self, name, nickname, superpower, health_points, damage, catchphrase):
        SuperHero.__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage

    def __str__(self):
        # метод, который
        # выводит прозвище героя, его суперспособность и его здоровье
        return f'{self.nickname}, {self.superpower}, {self.health_points},{self.damage}'

    def printPhrase(self):
        print('True in the True_phrase')

    def health_points2(self):
        # Изменить метод, который умножал хп героев на 2.
        self.health_points = int(self.health_points) ** 2
        self.fly = True


class Villain(Air, SuperHero):
    people = 'monster'

    def gen_x(self):
        pass

    def crit(self):
        self.damage = int(self.damage) * 2


print('3 дз')
hero2 = Air('Виктор Федоров', 'воздушный казак Вердена', 'летать на истребителе',200,20,'')
hero2.printPhrase()
print(f'Стало {hero2.health_points} здоровья у героя, умение летать {hero2.fly}')
hero2.health_points2()
print(f'Было {hero2.health_points} здоровья у героя, умение летать {hero2.fly}')
villain = Villain('Билл Шифер','Злой треугольник','телепортация, ясновидение,'
                                                  ' иллюзия, контроль физического тела',200,20,'Помни Реальность')
print(f'У злодея было {villain.damage} урона')
villain.crit()
print(f'Стало {villain.damage} урона')
try:
    hero2.crit()
except Exception as e:
    print(e)
