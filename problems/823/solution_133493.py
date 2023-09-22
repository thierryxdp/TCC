def faltante(lista):
    lista.sort()
    i = 0
    while i < len(lista):
        if len(lista) == 1:
            if lista[i] == 1:
                return lista[i] + 1
            else:
                return lista[i] - 1
        else:    
            if i == 0:
                if lista[i] != 1:
                    return 1
                else:
                    if lista[i+1] != lista[i] + 1:
                        return lista[i] + 1
            elif i < len(lista) - 1:
                if lista[i+1] != lista[i] + 1:
                    return lista[i] + 1
                    
            elif i == len(lista) - 1:
                if lista[i-1] != lista[i] - 1:
                    return lista[i] - 1
                else:
                    return lista[i] + 1
        i += 1