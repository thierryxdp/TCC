def maiores(lista, n):
    lista_retorno = [] 
    for elemento in lista:
        if elemento > n:
            lista_retorno.append(elemento) 
    return list.sort(lista_retorno)