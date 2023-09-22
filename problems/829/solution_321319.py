def soma_h(n):
    '''funcao que calcula a retorna H com duas casas decimais
    int->float'''
    H = 0
    for i in range(n):
        H = H + 1/(i + 1)
    return round(H, 2)