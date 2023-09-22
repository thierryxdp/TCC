def repetidos(lista):
    """esta função recebe uma lista e retorna o número de vezes que o elemento dessa é igual ao elemento anterior
    list-> int"""
    indice=0
    lista1=[]
    while indice<len(lista):
        if lista[indice]==lista[indice-1]:
            lista1+=[lista[indice]]
        indice+=1
    return len(lista1)