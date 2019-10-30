'''
Power Iteration method
'''
import operator
ITER_MAX = 100
EPS = 1e-6 # Raise EPS to big value to reach ITER_MAX

def p2d(mat):
    '''Pretty print 2d matrix'''
    for row in mat:
        print(row)


def pvec(vec):
    '''Print n x 1 vector'''
    PREC = 8
    print('[' + 
          '\n'.join(map(str, vec)) +
          ']'
         )


def getM(mat):
    # divide by outgoing nodes
    for i in range(len(mat)):
        mat[i] = list(map(lambda x: x/mat[i].count(1), mat[i]))

    # transpose
    ans = []
    for i in range(len(mat)):
        geti = operator.itemgetter(i)
        x = list(map(geti, mat))
        ans.append(x)
    return ans


def mul(mat, vec):
    # Multiply a 2d matrix with a 1d vector
    ans = []
    for i in range(len(mat)):
        y = sum(map(operator.mul, mat[i], vec))
        ans.append(y)
    return ans


if __name__ == '__main__':
    n = int(input('Enter no of  nodes'))
    print('Enter adjacency matrix')
    adj = []
    for _ in range(n):
        adj.append(list(map(int, input().split())))
    print('Adj:')
    p2d(adj)

    M = getM(adj)
    print('M:')
    p2d(M)

    # Initial page rank
    r = [1/n for _ in range(n)]
    print('R0')
    pvec(r)

    for _ in range(ITER_MAX):
        rx = r
        r = mul(M, r)

        # error is new - old
        error = list(map(operator.sub, r, rx))
        if all(map(lambda x: x < EPS, error)):
            print('EPS satisifed!')
            break
    else:
        print('ITER_MAX reached!')

    print('R')
    pvec(r)


'''
Figure 5.6
4
0 1 1 1
1 0 0 1
0 0 1 0
0 1 1 0
'''