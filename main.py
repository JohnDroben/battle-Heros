# Разработать консольную игру "Битва героев" на Python с использованием классов и разработать
# план проекта по этапам/или создать kanban доску для работы над данным проектом
## Общее описание:
# Создайте простую текстовую боевую игру, где игрок и компьютер управляют героями
# с различными характеристиками. Игра состоит из раундов, в каждом раунде игроки
# по очереди наносят урон друг другу, пока у одного из героев не закончится здоровье.
# Требования:
# Используйте ООП (Объектно-Ориентированное Программирование) для создания классов героев.
# Игра должна быть реализована как консольное приложение.
# Классы:
# Класс Hero:
# Атрибуты:
# Имя (name)
# Здоровье (health), начальное значение 100
# Сила удара (attack_power), начальное значение 20
# Методы:
# attack(other): атакует другого героя (other), отнимая здоровье в размере своей силы удара
# is_alive(): возвращает True, если здоровье героя больше 0, иначе False
# Класс Game:
# Атрибуты:
# Игрок (player), экземпляр класса Hero
# Компьютер (computer), экземпляр класса Hero
# Методы:
# start(): начинает игру, чередует ходы игрока и компьютера, пока один из героев не умрет.
# Выводит информацию о каждом ходе (кто атаковал и сколько здоровья осталось у противника)
# и объявляет победителя.

import time

class Hero():
    def __init__(self, name, health = 100, attack = 20):
        self.name = name
        self.health = health
        self.attack_power = attack

    def attack(self, other):
        self.health -= self.attack_power
        other.health -= self.attack_power
        print(f"{self.name} нанес {self.attack_power} урона {other.name}")
        print(f"{other.name} нанес {self.attack_power} урона {self.name}")
        print(f"{self.name} осталось {self.health} здоровья")
        print(f"{other.name} осталось {other.health} здоровья")


    def is_alive(self):
        return self.health > 0

class Game():
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def start(self):
        while self.player.is_alive() and self.computer.is_alive():
            print(f"Ход игрока {self.player.name}")
            self.player.attack(self.computer)
            print(f"Ход компьютера {self.computer.name}")
            self.computer.attack(self.player)
            time.sleep(1)

        if self.player.is_alive():
            print(f"Победил игрок {self.player.name}")
        else:
            print(f"Победил компьютер {self.computer.name}")



if __name__ == "__main__":

    player = Hero("Игрок")
    computer = Hero("Компьютер")
    game = Game(player, computer)
    game.start()