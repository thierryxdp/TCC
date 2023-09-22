def faltante(lista):
    """..."""
    list.sort(lista)
    posicao = 0
    contador = 0
    resultado= lista[-1]-contador
    while posicao < len(lista):
        if lista[posicao]-posicao == 2:
            contador = contador+1
        else:
            resultado = 'sla'
        posicao = posicao + 1
    return resultado