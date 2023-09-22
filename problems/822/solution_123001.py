def repetidos(lista):
    #Dado uma lista de números, retorna o número de vezes que um elemento da lista é igual ao elemento anterior. list -> int.
    contador = 0
    i = 1
    while i < len(lista):
        if lista[i] == lista[i-1]:
            contador += 1
        i += 1
    return contador