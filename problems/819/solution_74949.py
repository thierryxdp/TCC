def filtraMultiplos(lista,n):
    limitador= 0
    listaresp=[]
    while limitador < len(lista):
        if lista[limitador]%n==0:
            listaresp += [lista[limitador]]
        limitador+=1
    return listaresp