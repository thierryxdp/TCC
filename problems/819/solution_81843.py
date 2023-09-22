def filtraMultiplos(lista,n):
    lista_resposta = []
    i = 0
    while i<len(lista) :
        if lista[i] % n == 0:
            lista_resposta.append(lista[1])
        i += 1
    return lista_resposta