def repetidos(listaN):
    """recebe uma lista de numeros e retorna quantas vezes que um elemento da lista é igual
    ao elemento anterior;
    list->int"""
    i=0
    lista=[]
    while i<len(listaN)-1:
        if listaN[i]==listaN[i+1]:
            list.append(lista,True)
        else:
            list.append(lista,False)
        i = i+1
    return lista.count(True)