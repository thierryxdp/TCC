def soma_h(n):
    '''funcao que calcula o valor de H dada a soma  com n termos;
    int -> float'''
    H = 1
    for i in range(n):
        H += 1/n
    H = round(H,2)
    return H