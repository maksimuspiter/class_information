from random import choice


class A:
    def __str__(self):
        pass

    def __new__(cls, *args, **kwargs):
        print('news method')
        return super(A, cls).__new__(cls, *args, **kwargs)

    def __init__(self):
        pass

    x = 1


class Something:

    def __new__(cls, *args, **kwargs):
        print(f'конструируем: {args} | {kwargs}')

        instance = super().__new__(cls)

        # и вдруг нам захотелось добавить атрибут на лету
        instance.new_attribute = 'добавлено'

        print('почти готово')

        return instance

    def __init__(self, *args, **kwargs):
        print(f'инициализируем: {args} | {kwargs}')
        print(self.new_attribute)


class Distance(float):

    def __new__(cls, value, unit):
        """
            def __new__(cls, *args, **kwargs) - классика, редко нужен
            отрабатывает первый, нужен для расширения списка атрибутов класса (унаследованных)
            cls - ссылка на тип класса, должен возвращать cls


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

    def __sub__(self, other):
        if type(other) in [int, float, Distance]:
            self.value = float(self.value) - float(other)
            return self
        else:
            return 'Неправильный тип входного значения'


    def __add__(self, other):
        if type(other) in [int, float, Distance]:
            self.value = float(self.value) + float(other)
            return self
        else:
            return 'Неправильный тип входного значения'

