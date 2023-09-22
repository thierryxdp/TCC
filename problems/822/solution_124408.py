def repetidos(lista):
    """ Função que recebe uma lista de números e retorne as vezes que um elemento da lista é igual ao elemento antereior; list-> int"""
    i=0
    s=0
    while i<len(lista):
        if lista[i] not in lista[i]:
            s=s+str.count(lista[i])
            i=i+1
    return s