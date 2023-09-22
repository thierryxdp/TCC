def melhor_volta(m):
    lista = []
    i = 1
    for corredor in m:
        for valor in corredor:
            list.append(lista, valor)
   	
    	menor = min(lista)
        if menor in corredor:
            tupla = (i, menor, corredor.index(menor)+1)
        i = i + 1
    return tupla