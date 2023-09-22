def faltante (lista):
    '''função que recebe uma lista e retona qual número está
    faltando para completar a lista,list->int'''
    vari=0
    sindice=1
    pindece=0
    rodada=0
    while rodada>len(lista):
        if (lista[sindice])-(lista[pindece])==1:
            vari+=pindece
            vari+=sindice
        rodada+=1
    return vari