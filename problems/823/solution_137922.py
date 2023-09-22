def faltante (lista):
    '''função que recebe uma lista e retona qual número está
    faltando para completar a lista,list->int'''
    listaR=[]
    sindice=1
    pindece=0
    rodada=0
    while rodada>len(lista):
        if (lista[sindice])-(lista[pindece])==1:
            list.insert(listaR,pindece,lista[pindece])
            list.insert(listaR,pindece,lista[sindece])
        rodada+=1
        pindece+=1
        sindece+=1
    return listaR