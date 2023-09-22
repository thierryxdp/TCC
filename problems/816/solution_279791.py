def maiores(vetor,n):
    list.sort(vetor)
    copia = []
    
    for i in vetor:
        if(i > n):
            copia.append(i)

    return copia