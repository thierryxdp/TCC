def repetidos (lista_num):
    """Função que retorna o número de vezes que um elemento da lista é igual ao elemento anterior
    dada uma lista de números.
    list -> int"""
    i = 0
    repetidos = 0
    while i < len(lista_num):
        if lista_num[i] == lista_num[i]:
            repetidos = repetidos + 1
            i = i+1
        i = i+1
    return repetidos