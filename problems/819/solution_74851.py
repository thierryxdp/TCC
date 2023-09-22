def filtraMultiplos(lista,n):
    """Dado uma lista e um número n, a função retorna uma lista com todos os múltiplos de n contidos na lista de entrada;
    list,int->list"""
    indice1=0
    quantidade=[]
    while indice1<len(lista):
        if lista[indice1]%n==True:
            list.append(quantidade,indice1)
            indice1=indice1+1
        else:
            indice1=indice1+1
    indice2=0
    novalista=[]
    while indice2<len(quantidade):
        soma=quantidade[indice2]
        list.append(novalista,soma)
        indice2=indice2+1
    return novalista