def filtraMultiplos(lista,n):
    '''Calcula e retorna uma lista contendo apenas números divisíveis por n, utilizando uma lista com números como entrada.
    list,int-->list'''
    i=0
    multi=[]
    while i<len(lista):
        resto=lista[i]%n
        if resto==0:
            multi= multi+[lista[i]]
            return multi
         i=i+1
    return multi