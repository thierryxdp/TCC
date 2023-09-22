def faltante(lista):
    """..."""
    list.sort(lista)
    posicao = 0
    resultado = 0
    
    while posicao < len(lista)-1:
        if lista[posicao] != lista[posicao+1]:
            resultado = lista[posicao+1]
        posicao = posicao + 1
        
    return resultado