def faltante(lista):
    i = 0
    #falt = int(lista[i] < falt < lista[i + 1])
   # print(lista)
    while i < len(lista)+1:
        if 1 not in lista:
            return 1
        else:
            list.sort(lista)
            d = lista[i+1] - lista[i]
            if d > 1:
                return lista[i]+1
        i += 1