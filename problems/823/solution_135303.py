def faltante(lista):
    x=0
    i=0
    while lista[i]+2!=lista[i+1]:
        x=lista[i]+2
        i=i+1
    return x