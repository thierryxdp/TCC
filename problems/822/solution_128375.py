def repetidos(lista):
    """funcao que recebe uma lista de numeros e retorna o
numero de vezes que um elemento da lista é igual ao elemento
anterior
list->int"""
    i=0
    numero_vezes = 0
    while i+1<len(lista):
        if lista[i] == lista[i+1]:
            numero_vezes = numero_vezes + 1
        i = i+1
    return numero_vezes