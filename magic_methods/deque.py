class Queue:

    @staticmethod
    def get_rais_error():
        raise IndexError('No this index')

    def __init__(self):
        self.__length = 0
        self.__head = -1
        self.__tail = 0

    def __str__(self):
        if self.__length:
            if self.__head >= self.__tail:
                return f"queue<{self.__queue[self.__tail:self.__head + 1]}>"
            else:
                return f"queue<{self.__queue[self.__tail:] + self.__queue[:self.__head+1]}>"
        else:
            return f"queue<[]>"

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls, *args, **kwargs)
        instance.__queue = [None] * 8
        return instance

    def __len__(self):
        return self.__length

    def append(self, element):
        if self.__length < 8:
            self.__head += 1
            self.__queue[self.__head] = element
            self.__length += 1
        else:
            self.get_rais_error()

    def append_back(self, element):
        if self.__length < 8:
            if self.__tail == 0:
                self.__tail = 7
                pass
            else:
                self.__tail -= 1
            self.__queue[self.__tail] = element
            self.__length += 1
        else:
            self.get_rais_error()

    def pop_right(self):
        if self.__length:
            self.__length -= 1
            el = self.__queue[self.__head]
            self.__queue[self.__head] = None
            return el
        else:
            self.get_rais_error()

    def pop_left(self):
        if self.__length:
            self.__length -= 1
            el = self.__queue[self.__tail]
            self.__queue[self.__tail] = None
            return el
        else:
            self.get_rais_error()

print('fff')