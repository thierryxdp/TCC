def faltante (lista):
    
    seguinte = 0
    faltante= 0
    list.sort(lista)
    while seguinte < len(lista):
        if lista[seguinte] != (lista[seguinte] + 1):
             faltante=  lista[seguinte] +1
        seguinte= seguinte + 1
    return faltante