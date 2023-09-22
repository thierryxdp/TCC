def soma_h(N):
    """funcao que calcula e retorna a soma do valor H"""
    """int->float"""
    lista=list(range(1,N+1))
    numeros=0
    for numero in lista:
        numeros = numeros + 1/numero
    return round(numeros,2)