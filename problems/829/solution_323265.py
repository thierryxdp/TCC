def soma_h(n):
    """dado um numero n de entrada retorna uma sequencia de
    numeros de 1 sobre 1 até n
    int-->float"""
    h=0
    for i in range(1,n+1):
        h=h+1/i
    return h