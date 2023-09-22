def filtraMultiplos(lista:list,n:float):
    lista_resposta = []
    while i<len(lista) :
        if lista[i] % n == 0:
            lista_resposta.append(lista[1])
            i += 1
    return lista_resposta