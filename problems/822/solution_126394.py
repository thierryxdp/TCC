def repetidos(lista):
    """ Função que dada uma lista, retorna o número de vezes que um elemento da lista é igual ao anterior
    list -> int """
    i=0
    conta=0
    while i<len(lista):
        if lista[i-1]==lista[i]:
            conta=conta+1
        i=i+1
    return conta