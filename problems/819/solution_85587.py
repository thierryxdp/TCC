def filtraMultiplos(lista,multiplo):
    '''função que retorna a lista de numeros multiplos de um elemento;
        list,int->list'''
    contador=0
    filtro=[]
    while contador<len(lista):
        if lista[contador]%multiplo==0:
            filtro+=[lista[contador]]
            contador+=1
        else:
            contador+=1
    return filtro