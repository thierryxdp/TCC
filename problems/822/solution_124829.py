def repetidos(lista):
    '''recebe como entrada uma lista de números
e retorne o número de vezes que um elemento 
da lista é igual ao elemento anterior'''
    indice=1
    vezes=0
    while indice<len(lista):
        if lista[indice]==lista[indice-1]:
            vezes+=1
        indice+=1
    return vezes