def filtraMultiplos(lista,num):
    '''recebe como entrada uma lista de números e um número,
e retorna outra lista contendo todos os elementos da lista 
original que forem divisíveis por n.'''
    multiplos=[]
    indice=0
    while indice<len(lista):
        if lista[indice]%num==0:
            multiplos=multiplos+[lista[indice]]
        indice+=1
    return multiplos