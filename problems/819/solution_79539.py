def filtraMultiplos(lista,n):
    '''
    '''    

    listaN=[]
    divisao=  lista/n
    resto= n *divisao==lista

    while len(lista)<len(lista[-1]):
        divisao= lista/n
        resto= n *divisao==lista

    return listaN