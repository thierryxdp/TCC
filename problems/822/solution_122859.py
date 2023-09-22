def repetidos(lista):
    """Recebe uma lista de números como entrada e retorna o número de vezes 
    que um elemento da lista é igual ao anterior"""
    contador = 0
    atual = anterior = 0
    vezes = 0
    while contador < len(lista):
        if contador == 0:
            atual = lista[contador]
        else:
            atual = lista[contador]
            if anterior == atual:
                vezes += 1
        anterior = atual
        contador += 1
    return vezes