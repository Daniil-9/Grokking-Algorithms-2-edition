def summ(t, i=0):
    if i == len(t):
        return 0
    return t[i] + summ(t, i + 1)

t = [2, 4, 6]
print(summ(t))