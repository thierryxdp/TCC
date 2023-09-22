def filtraMultiplos(lista, n):
'funcao recebe uma lista com numeros e os separa so com os multiplos do numero N'    
    ret = []
    for i in lista:
        if i%n==0:
            ret.append(i)
    return(ret)