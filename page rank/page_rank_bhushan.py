import pprint
import string
import numpy as np


dp = pprint.pprint if True else lambda *x,**y: None

DATA = [[1, 0, 1, 1, 0],
        [1, 0, 0, 1, 0],
        [0, 0, 1, 1, 1],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0]]

def check(r1, r2, eps=1):
    tot = 0
    for a, b in zip(r1, r2):
        tot += (a[0] - b[0])
    if tot < eps:
        return True
    return False

def transpose(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

def generate_M(data):
    for i in range(len(data)):
        try: 
            data[i] = list(map(lambda x: round(x/data[i].count(1), 2), data[i]))
        except Exception as e:
            pass
    return transpose(data)

def page_rank(data, max_iter=100):
    M = generate_M(data)
    print(f'M: {M}')
    r = transpose([[round(1/len(data), 2)]*len(data)])
    print(f'r: {r}')

    for i in range(max_iter):
        new_r = list(map(list, np.matmul(M, r)))
        if check(new_r, r):
            dp('converged')
            break
        else:
            continue

    print(f'Final Page Ranks: {new_r}')


if __name__ == '__main__':
    # n = int(input('Enter number of nodes: '))
    # data = []
    # print('Enter Adjacency Matrix')
    # for i in range(n):
    #     arr = list(map(int, input(f'Enter for row {i+1}: ').split()))
    #     data.append(arr)
    page_rank(DATA)
