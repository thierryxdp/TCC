def maiores(inteiros, n):
    inteiros = []
    n = 0
    sublista = []
    for i in range(inteiros):
        if n > i:
            n = n +1
            sublista = list.append(n , sublista)
    return sublista