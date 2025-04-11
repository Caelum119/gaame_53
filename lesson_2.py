# Hi Senseiddehowehuheuwihfew

class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__was_born()

    def __was_born(self):
        print(f'Animal {self.__name} was born.')

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if type(age) == int and age > 0:
            self.__age = age
        else:
            raise ValueError('age must be positive integer')

    def info(self):
        return (f'{self.__name} is {self.__age} years old. '
                f'Birth year: {2025 - self.__age}')

    def make_voice(self):
        raise NotImplementedError('Method not implemented')


class Fish(Animal):
    def __init__(self, name, age):
        super(Fish, self).__init__(name, age)

    def make_voice(self):
        pass


class Cat(Animal):
    def __init__(self, name, age):
        # super().__init__(name, age)
        super(Cat, self).__init__(name, age)

    def make_voice(self):
        print('Myau')


class Dog(Animal):
    def __init__(self, name, age, commands):
        super(Dog, self).__init__(name, age)
        self.__commands = commands

    @property
    def commands(self):
        return self.__commands

    @commands.setter
    def commands(self, commands):
        self.__commands = commands

    def info(self):
        return super().info() + f' Commands: {self.__commands}'

    def make_voice(self):
        print('Gav')


class FightingDog(Dog):
    def __init__(self, name, age, commands, wins):
        super(FightingDog, self).__init__(name, age, commands)
        self.__wins = wins

    @property
    def wins(self):
        return self.__wins

    @wins.setter
    def wins(self, value):
        self.__wins = value

    def info(self):
        return super().info() + f' Wins: {self.__wins}'

    def make_voice(self):
        print('Rrr gav')


# some_animal = Animal('Anim', 2)
# print(some_animal.get_name())
# some_animal.set_age(4)
# print(some_animal.info())

fish = Fish('Nemo', 2)

cat = Cat('Murka', 3)
# print(cat.info())

dog = Dog('Snoopy', 5, 'Sit')
# print(dog.info())
# dog.commands = 'Sit, bark'
# print(dog.commands)

fightingDog = FightingDog('Reks', 1, 'Fight', 9)
# print(fightingDog.info())

animals_list = [fish, cat, dog, fightingDog]
for animal in animals_list:
    print(animal.info())
    animal.make_voice()

print('End')
