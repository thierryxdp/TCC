def repetidos(lista):
    """Função que retorna o número de vezes que um elemento da lista dada como entrada é igual ao elemento anterior a ele
lista -> int"""

    repetidos = []
    anterior = 0

    while anterior <len(lista):
        if lista[anterior] == lista[anterior - 1]:
            repetidos = repetidos + [lista[anterior],]
        anterior = anterior + 1
    return len(repetidos)