def faltante(lista):
    """retorna o numero faltante da sequencia da lista dada """
    lista.sort()
    atual = []
    proximo = []
    cont = 1
    i = 0
    if lista[0] == 1:
        while i < len(lista):
            if cont < len(lista):
                proximo = lista[cont]
                atual = lista[i]
                if proximo == atual+1:
                    cont += 1
                else:
                    cont += 1
                    break
            else:
                cont += 1
            i += 1
    else:
        cont = 1
    return cont