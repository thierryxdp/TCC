def soma_h(n):
    """ Função que calcula e retorna o valor de H com N termos
    N é meu valor int de entrada"""
    H = 0
    for i in range(1, n+1):
        H += 1/i 
    return round(H, 2)