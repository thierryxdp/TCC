def repetidos(lista):
    repetido=0
    i=0
    list.append(lista,'0')
    while i<(len(lista)-1):
        if lista[i]==lista[i+1]:
            repetido=repetido+1
        i=i+1
        elif lista[i-1]==lista[i]:
            repetido=repetido+1
        i=i+1
    return repetido