def repetidos(lista):
    """
       """
    contador = 0
    repetidos = 0
    anterior = 0
    atual = 0 
    while contador < len(lista):
        if contador == 0:
            atual = lista[contador]
        else:
            atual = lista[contador]
            if anterior == atual:
                vezes = vezes + 1
        anterior = atual
        contador = contador + 1
    return vezes