def primo(n):
    for i in range(n):
        if i % 1 == 0 and i % n == 0:
            k = 0
        else:
            k = 1
    return k==0