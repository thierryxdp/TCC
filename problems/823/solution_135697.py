def faltante(lista):
    lista_corrigida = lista.sort
    auxiliar= []
    i = 1
    while i<=len(lista_corrigida)+1:
        auxiliar = auxiliar + [[i],]
    i = i + 1
    return sum(auxiliar[0],auxiliar[-1]) - sum(lista_corrigida[0],lista_corrigida[-1])