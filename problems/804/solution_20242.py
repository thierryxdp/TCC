def filtra_pares(a,b,c,d):
    '''função que recebe os valores a,b,c e d e retorna os pares'''
    lista1=[a,b,c,d]
    lista2=filter(lambda x: x%2==0, lista1)
    
    
    return (lista2,)