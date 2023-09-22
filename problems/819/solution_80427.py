def filtraMultiplos(lista,N):
    listaNumerosMultipolsN=[]
    a=0
    listaCopia=lista[:]
    while a<len(listaCopia):
        if lista[a]%N==0:
            listaNumerosMultipolsN=listaNumerosMultipolsN+[lista[a]]
        a=a+1
    return listaNumerosMultipolsN