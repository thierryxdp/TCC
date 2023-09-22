def filtraMultiplos(lista,num):
    multiplos=[]
    for el in lista:
        if el%num==0:
            multiplos=multiplos+[el,]
    return multiplos