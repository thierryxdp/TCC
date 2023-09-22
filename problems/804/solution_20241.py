def filtra_pares(a,b,c,d):
    '''função que recebe os valores a,b,c e d e retorna os pares'''
    lista1=[a,b,c,d]
    (a1,b1,c1,d1)=filter(lambda x: x%2==0, lista1)
    
    
    return (a1,b1,c1,d1)