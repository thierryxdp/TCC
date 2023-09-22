def faltante (lista):
    '''função que recebe uma lista e retona qual número está
    faltando para completar a lista,list->int'''
    listaR=[]
    sindice=1
    pindece=0
    rodada=0
    while True:
        if (lista[sindice])-(lista[pindece])==1:
            listaR+=pindece
            listaR+=sindice
        rodada+=1
    return listaR