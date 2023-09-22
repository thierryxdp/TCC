def repetidos(lista_numeros):
    i=1
    rep=0
    while i<len(lista_numero)-1:
        if lista_numeros[i]==lista_numeros[i+1]:
            rep=rep+1
        i=i+1
    return rep