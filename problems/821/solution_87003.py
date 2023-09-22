def fatorial(num):
    """Dado um número, esta fução calcule seu fatorial; int-> int"""
    posicao = 0
    resultado = 1
    lista = list(range(num,0,-1))
    
    while posicao < len(lista):
        resultado = resultado * lista[posicao]
        posicao = posicao + 1
        
    return resultado