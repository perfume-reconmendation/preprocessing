import multiprocessing

from multiprocessing import Pool

def f(x):
    return x*x


def mul():
    with Pool(5) as p:
        return p.map(f, [1, 2, 3])

if __name__ == '__main__':
    print(mul())
    