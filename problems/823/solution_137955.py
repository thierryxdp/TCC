def faltante (lista):
    '''função que recebe uma lista e retona qual número está
    faltando para completar a lista,list->int'''
    listaR=0
    sindice=1
    pindece=0
    rodada=0
    while rodada>len(lista):
        if (lista[0])-(lista[1])!=1:
            break
        rodada+=1
        pindece+=1
        sindece+=1
    return ((lista[sindice])+(lista[pindece])+1)