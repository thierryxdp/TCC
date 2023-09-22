def filtraMultiplos(lista, m):
    matue=[]
    for elemento in lista:
        if elemento%m==0 and m in lista:
            matue=matue+elemento+m
        elif elemento%m==0 and m not in lista:
            matue=matue+elemento
        else:
            matue=matue
    return matue