def filtraMultiplos(lista_num, num):
    multiplos = []
    i=0
    while i<len(lista_num):
        if lista_num[i]%num==0:
            list.append(multiplos,lista_num[i])
            i=i+1
        else:
            i=i+1
    return multiplos