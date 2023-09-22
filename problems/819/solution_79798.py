def filtraMultiplos(lista, num):
    '''Função que dada uma lista de números, irá retornar uma outra lista com apenas os números multiplos do número n(entrada). list, int -> list '''
    i=0
    lista1=[]
    while i<len(lista):
        if lista[i]%num==0:
            lista1=lista1+[lista[i],]
            i=i+1
        else:
            i=i+1
    return lista1