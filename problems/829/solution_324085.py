def soma_h(n):
    '''funcao que calcula o valor de H dada a soma  com n termos;
    int -> float'''
    H = round(H,2)
    for i in range(n + 1):
        H = H + 1/n
    return H