def repetidos(lista):
    """ Função que recebe uma lista de números e retorne as vezes que um elemento da lista é igual ao elemento antereior; list-> int"""
    i=0
    s=0
    while i<len(lista):
        if lista[i]==lista[i-1]:
            s=s.count()
            i=i+1
    return s