from typing import List, Union


def secti_prvky(seznam: List[int]) -> int:
    soucet = 0
    for prvek in seznam:
        soucet += prvek
    return soucet


def soucet(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    return x + y


a: int = 1
b: float = 2.1

c = soucet(a, b)

print(c)

print(secti_prvky([1, 2, 3, 4, 5]))
