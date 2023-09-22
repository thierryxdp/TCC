def repetidos(lista):
    """ retorna o número de vezes que um elemento da lisya é igual ao anterior;
    list->int"""
    i=0
    x=0
    lista2=lista[i-1:i]
    while(i<len(lista)):
        if [i] in lista2:
            x+=1
    i+=1
    return x