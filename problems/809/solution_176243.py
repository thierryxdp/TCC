def intercala(lista1, lista2):
    """funcao que dadas duas listas de tamanho 3 retorna uma lista que intercala os elementos das duas listas dadas;
       list,list->list"""
    [num1,num2,num3]=lista1
    [num4,num5,num6]=lista2
    lista1[1]=num4
    lista1[2]=num2
    lista2[0]=num5
    lista2[1]=num3
    return lista1+lista2