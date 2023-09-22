def soma_H(n):
    '''funcao que calcula o valor de H dada a soma  com n termos;
    int -> float'''
    H = 1
    for i in range(n + 1):
        H += 1/n
    return H