def repetidos(listaV):
    """recebe uma lista de numeros e retorna o numero 
    de vezes que um elemento da lista é igual ao elemento
    anterior. list->int"""
    cont=0
    t=1
    while t<len(listaV):
        if listaV[t]==(listaV[t-1]):
            listaV.count(listaV[t])
            cont+=1
        t+=1
    return cont