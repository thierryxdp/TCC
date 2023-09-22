def repetidos(lista):
    """ retorna o número de vezes que um elemento da lisya é igual ao anterior;
    list->int"""
    i=0
    x=0
    while(indice<len(lista)):
        if [indice] in lista[indice-1:indice]:
            x+=1
    i+=1
    return x