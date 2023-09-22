def faltante(L):
    list.sort(L)
    i = len(L)
    listaCerta = list(range(1,i+2))
    listaFaltantes = []
    h = 0
    while h+1<len(listaCerta):
        
        if L[h] != listaCerta[h]:
            listaFaltantes.append(listaCerta[h])
        h = h + 1
    return int(listaFaltantes[0])