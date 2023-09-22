def soma_h(n):
    '''funcao que calcula o valor de H dada a soma  com n termos;
    int -> float'''
    H = 1
    for i in list(range(n + 1)):
        H = H + 1/n
    return round(H,2)