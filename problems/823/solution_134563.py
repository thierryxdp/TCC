#
#
#
#
def faltante(lista):
    i=0
    list.sort(lista)
    maior=max(lista)
    menor=min(lista)
    while i < len(lista):
        if (lista[i+1]-lista[i])==1:
            i=i+1
            falta=lista[i]
            return falta
        elif [menor-1] in lista:
            return maior
    return menor