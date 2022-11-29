# Задание №1 с интеграцией функции func_chain
def sequential_map(*args):
    return func_chain(*args[:-1])(args[-1])

# Задание №2
def consensus_filter(*args):
    ans, funs, arr = [], args[:-1], args[-1]
    for x in arr:
        if int(sum([f(x) for f in funs])) == len(funs):
            ans.append(x)
    return ans

# Задание №3
def conditional_reduce(f1, f2, arr):
    tmp = [x for x in arr if f1(x)]
    ans = tmp[0]
    for i in range(1, len(tmp)):
        ans = f2(ans, tmp[i])
    return ans

# Задание №4
def func_chain(*args):
    def help(x):
        for f in args:
            if type(x) == type([]) or type(x) == np.ndarray:
                x = list(map(f, x))
            else:
                x = f(x)
        return x
    return help

# Дополнительное Задание №2
import sys

def my_print(s):
    if type(s) == str:
        sys.stdout.write(s)
    elif type(s) in [int, float, bool]:
        sys.stdout.write(str(s))
    else:
        for c in s:
            sys.stdout.write(str(c) + ' ')
    sys.stdout.write('\n')