def repetidos(lista):
    'função que retorna número de vezes que um elemento de uma lista é igual ao elemento anterior. list->int'
    cont=0
    i=-1
    while i<-len(lista):
        if lista[i]==lista[i-1]:
            cont+=1
        i+=1
        return cont