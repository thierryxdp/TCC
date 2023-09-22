def filtraMultiplos(lista_num,n):
    i=0
    lista_multiplos=[]
    while i<len(lista_num):
        if lista_num[i]%n == 0:
            lista_multiplos.append(lista_num[i])
        i=i+1
    return lista_multiplos