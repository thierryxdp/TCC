def filtraMultiplos(lista_num,n):
    i=0
    lista_multiplos=[]
    while i<len(lista_num):
        if lista_num[i]%n == 0:
            lista_multiplos = lista_num[i]+lista_multiplos
        i=i+1
    return lista_multiplos