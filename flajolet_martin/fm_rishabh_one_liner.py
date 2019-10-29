hash_fn = lambda x: (3 * x + 1) % 5


def fm(inp, hash_fns=(hash_fn, )):
    """
    inp: iterable of ints
    hash_fns: list of callables with one ip.
    """
    last_set_value = lambda n: (n & ~(n - 1))  # face value of last set bit
    est = [max(map(lambda x: last_set_value(hfn(x)), inp)) for hfn in hash_fns]
    print(f"Average estimated unique values: {sum(est) / len(est)}")


if __name__ == '__main__':
    inp = [10, 12, 13, 3, 4, 25, 7, 10, 4]
    fm(inp)

