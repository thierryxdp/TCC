def soma_h(N):
    """Função que calcula e retorna o valor H
    com N termos onde N é inteiro e dado como
    entrada"""
    H = 0
    for numeros in list(range(1,N+1)):
        H = H + 1/numeros
    return round(H,2)