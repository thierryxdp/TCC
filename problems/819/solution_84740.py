def filtraMultiplos(lista_n,n):
    x = 0
    contador = 0
    lista = []
    
    while contador <len(lista_n):
        
        posicao = lista_n[x]
        if posicao%n == 0:
            lista.append(posicao)
        contador = contador + 1
        x = x+1

    return lista