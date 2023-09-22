def primo(N):
    F = 0
    NUM = 1
    while N != NUM:
        if N % NUM == 0:
            F = F + 1
        N = N + 1
    if F = 2:
        return True
    else:
        return False