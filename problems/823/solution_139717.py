def faltante(lista):
    list.sort(lista)
    i= 0
    while i< len(lista):
        if len(lista)== 1 and 1 <lista[0] <3:
            x= lista[0] -1
            return x
        if lista[i] -1 not in lista and lista[i]>1:
            x= lista[i] -1
            return x
        if lista[i] +1 not in lista:
            x= lista[i] +1
            return x 
        i=i+1