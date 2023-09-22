def soma_h(N):
    F1=0
    NUM = 1
    while NUM < N+1:
        F = 1/NUM
        F1 = F1 + F
        NUM = NUM + 1
    return round(F1,2)