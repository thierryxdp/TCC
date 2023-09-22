def maiores(lista, n):
     lista_retorno = []
    for elemento in lista:
        if elemento > n:
            lista_retorno.append(elemento)  
    lista_retorno.sort()
    return lista_retorno