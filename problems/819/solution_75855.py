def filtraMultiplos(lista,num):
    ''' '''
    lista0=[]
    multiplo=0
    while multiplo < len(lista):
        if (lista[multiplo]%num)==0:
            lista0=lista0+[lista[multiplo],]
        multiplo=multiplo+1
    return lista0