# 1)создать класс SuperHero
class SuperHero:
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
