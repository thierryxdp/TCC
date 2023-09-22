def melhor_volta(m):
    lista = []
    i = 1
    for corredor in m:
        for valor in corredor:
            list.append(lista, valor)
   	
    menor = min(lista)
    for corredor in m:
        if menor in corredor:
            tupla = (i, menor, corredor.index(menor))
        i = i + 1
    return tupla