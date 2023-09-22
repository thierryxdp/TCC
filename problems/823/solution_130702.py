def faltante(lista):
    indice=0
    x=lista[-1]+1
    while indice<len(lista):
        if lista[0]==2:
            return 1
        elif len(lista)==len(range(1,x)):
            return lista[-1]+1
        elif lista[indice]+1==lista[indice+1]:
            indice=indice+1
        else:
            return lista[indice]+1