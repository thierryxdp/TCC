def faltante(lista):
    minim = min(lista)
    maxim = max(lista)
    lista_maxima = list(range(minim,maxim+1))
    soma_maxima = sum(lista_maxima)
    soma_lista = sum(lista)
    
    return soma_maxima - soma_lista