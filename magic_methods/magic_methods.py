from random import choice

"""
Методы: __new__(cls, *args, **kwargs)
        __init__(self, *args, **kwargs)
        __str__(self)
        __sub__(self, other)
        __add__(self, other)
"""


class Distance(float):

    def __new__(cls, value, unit):
        """
            def __new__(cls, *args, **kwargs) - классика, редко нужен
            отрабатывает первый, нужен для расширения списка атрибутов класса (унаследованных)
            cls - ссылка на тип класса, должен возвращать cls

            Метод ----> @staticmethod, указывать не нужно (по умолчанию в object)


            !!! Можно использовать для ссылки(наследования) на другой класс, с целью стать его ребенком
            ##########################################################################################
            ## класс может выбрать родителя случайным образом, при этом его метод __init__ не выполнится
            class Pet:
                def __new__(cls):
                    other = choice([Dog, Cat, Bird])
                    instance = super().__new__(other)
                    print(f"I am {type(instance).__name__}")
                    return instance

                def __init__(self):
                    print("Never called")


            class Dog:
                def communicate(self):
                    print("gav")


            class Cat:
                def communicate(self):
                    print("mia")


            class Bird:
                def communicate(self):
                    print("chik")


            for _ in range(5):      ######################################################################
                pet = Pet()         ### В цикле будут создаваться новые экземпляры класса с различными ###
                pet.communicate()   ### родителями и методами                                          ###
                ##########################################################################################
        """
        instance = super().__new__(cls, value)
        instance.unit = unit
        return instance

    def __init__(self, value, unit):
        """
        Метод инициализации (превращение атрибутов в атрибуты класса)
        можно инициализировать аргументы, которые не передавали
        аргументы будут относиться к атрибуту экземпляра
        """
        self.value = value
        self.unit = unit
        self.arg_self = 'My_arg'

    # возвращает значение при обращении к экземпляру класса
    def __str__(self):
        """
        Метод для представления экзепляра (что будет отображаться, при обращении к нему)
        """
        return f"{self.value} {self.unit}"

    def __del__(self):
        """
        Описывает действия при удалении экземпляра.
        Автоматически вызывается в Python, когда экземпляр собираются уничтожить.
        Вызывается для любого объекта, когда счетчик ссылок для этого объекта становится равным нулю.
        """
        print('Object destroyed')

    def __sub__(self, other):
        """
            Метод описывающий операцию вычитания
        """
        if type(other) in [int, float, Distance]:
            self.value = float(self.value) - float(other)
            return self
        else:
            return 'Неправильный тип входного значения'

    def __add__(self, other):
        """
                    Метод описывающий операцию сложения
                """
        if type(other) in [int, float, Distance]:
            self.value = float(self.value) + float(other)
            return self
        else:
            return 'Неправильный тип входного значения'


class A(object):
    pass