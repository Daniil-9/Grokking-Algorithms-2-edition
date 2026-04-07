def summ(t):
    if len(t) == 0: return sum(t)
    else: return t[0] + summ(t[1:])

def countt(t):
    if len(t) == 0: return 0
    else: return 1 + countt(t[1:])

def maxi(t):
    if len(t) == 1: return t[0]
    return t[0] if t[0] > maxi(t[1:]) else maxi(t[1:])

t = [2, 4, 6]

print(summ(t))
print(countt(t))
print(maxi(t))