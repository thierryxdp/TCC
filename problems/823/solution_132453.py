def faltante(lista):
    """Funcao que retorna o numero faltante dentro da lista fornecida;
    list -> int"""

    list.sort(lista)
    ultimoindice = lista[-1]+1
    listacompleta = list(range(1,ultimoindice))
    i = 0

    while i < len(listacompleta):
        if listacompleta[i] in lista:
            i+=1
        elif listacompleta[i] not in lista:
            return listacompleta[i]