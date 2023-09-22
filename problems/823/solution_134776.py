def faltante(lista):
    i=0
    while lista[i]+1!= lista[i+1]:
        i=i+1
    return lista[i]+1