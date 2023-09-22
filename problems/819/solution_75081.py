def filtraMultiplos(lista,n):
    '''Função que recebe uma lista e um número e retorna uma nova lista com os elementos divisíveis por n
       list,int->int'''
    aux=[]
    lista = range(1,n+1)
    for var in lista:
        if n%var==0:
            aux.append(var)
    return aux