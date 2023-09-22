def faltante(lista):
    l=lista[:]
    l.sort()
    contador=0
    while contador <len(l):
        if l[contador]==contador+1:
            contador+=1
        else:
            return l[contador]