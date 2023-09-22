def filtraMultiplos(lista,n):
    '''retorna todos os números da lsita que forem múltiplos de n
    lista,int->lista'''
    
    return list(filter(lambda x: x%n==0,lista))