def repetidos(lista):
    """Função que retorna o número de vezes que um elemento da lista é igual ao elemento anterior. list -> int"""
    i=1
    vezes=0
    while i<len(lista):
        if lista[i]==lista[i-1]:
            i+=1
            vezes+=1
        else:
            i+=1
    return vezes