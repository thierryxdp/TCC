def repetidos(lista):
    """ retorna o número de vezes que um elemento da lisya é igual ao anterior;
    list->int"""
    i=0
    x=0
    while(i<len(lista)):
        if [i] in lista[i-1:i]:
            x+=1
    i+=1
    return x