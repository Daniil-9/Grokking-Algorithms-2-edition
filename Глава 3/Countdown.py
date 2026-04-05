def countdown(i):
    print(i)
    if i <= 1:      # базовый случай
        return
    else:           # рекурсивный случай
        countdown(i-1)

countdown(3)