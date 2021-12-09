import sys
import builtins


def printw(*args):
    strings = map(str, args)
    print(" ".join(strings))


def printf(_format, *args):
    sys.stdout.write(_format % args)


def scanf(s):
    values = []
    for f in s.split():
        prompt = "[" + f[1] + "]? "
        if f == "%s":
            values.append(input(prompt))
        elif f == "%d":
            values.append(int(input(prompt)))
        elif f == "%f":
            values.append(float(input(prompt)))
    if len(values) == 1:
        return values[0]
    return values


class Array:
    def __init__(self, size1=0, size2=0, all_elements=0, rep=False, tab=None):
        if rep:
            if size2 > 0: self.__items = [Array(size1, rep=True) for _ in range(size2)]
            else: self.__items = list(range(0, size1))
        elif tab:
            self.__items = tab
            self.__sizes = self.__see_dimentions(tab, [])
        else:
            self.__sizes = (size1, size2)
            if size2 > 0:
                self.__items = [Array(size1, all_elements=all_elements) for _ in range(size2)]
            else:
                self.__items = size1 * [all_elements]

    def __setitem__(self, i, x):
        if i < 0 or i >= len(self.__items):
            raise "Array index out of range"
        self.__items[i] = x

    def __getitem__(self, i):
        if i < 0 or i >= len(self.__items):
            raise "Array index out of range"
        return self.__items[i]

    def __len__(self):
        if self.__sizes[1]:
            return self.__sizes
        return self.__sizes[0]

    def __see_dimentions(self, tab, dim):
        try:
            dim.append(len(tab[0]))
            return self.__see_dimentions(tab[0], dim)
        except IndexError:
            return dim

    def print(self):
        if self.__sizes[1]:
            print('[')
        else:
            print('[', end='\t')
        for i in range(self.__sizes[0]):
            if self.__sizes[1]:
                print(end='\t')
                self.__print(self[i])
            else:
                print(self[i], end='\t')
        print(']')

    @staticmethod
    def __print(array):
        print('[', end='\t')
        for el in array.__items:
            print(el, end='\t')
        print(']')


class ListItem:
    def __init__(self, value):
        self.value = value
        self.next = None


class TreeItem:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def none():
    return None

builtins.min = none
builtins.max = none
builtins.bin = none
builtins.all = none
builtins.any = none
builtins.eval = none
builtins.hex = none
builtins.oct = none
builtins.sum = none
