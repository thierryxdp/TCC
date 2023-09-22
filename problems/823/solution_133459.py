def faltante(lista):
    lista.sort()
    i = 0
    while i < len(lista):
        if i < len(lista) - 1:
            if lista[i+1] == lista[i] + 1:
            continue
            else:
                return lista[i]+1
                
        elif i == len(lista) - 1:
            if lista[i-1] == lista[i] - 1:
                continue
            else:
                return lista[i] - 1
            
        i += 1