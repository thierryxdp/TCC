def filtraMultiplos(lista:list,n:float):
    i = 0
    lista_resposta = []
    while i<=len(lista):
        if lista[i] % n == 0:
            lista_resposta.append(lista[1])
        i = i + 1   
    return lista_resposta