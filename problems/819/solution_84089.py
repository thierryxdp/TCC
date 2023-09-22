def filtraMultiplos(listaNumeros, n):
    novaLista = []
    
    i = 0
    while i < len(listaNumeros):
        if listaNumeros[i] % n == 0:
            novaLista.append(listaNumeros[i])
            
        i += 1
    return novaLista