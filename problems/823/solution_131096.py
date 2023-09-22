def faltante(lista):
    """..."""
    list.sort(lista)
    posicao = 0
    resultado = 0
    
    while posicao < len(lista):
        if lista[posicao]-posicao == 2:
            resultado = lista[posicao]-1
        else:
            resultado = 'sla'
    return resultado