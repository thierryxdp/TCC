def repetidos(lista):
    '''essa lista tem como objetivo verificar se existe na lista números
    repetidos, e compara sempre com o seu anterior, e dar como resposta
    o número de repetições que ocorre'''
    '''list -> int'''
    
    i= 0
    rep = 0
    while lista[i] == lista[i-1]:
        rep = rep + 1
    return rep