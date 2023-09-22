def maiores(lista, n):
    lista_retorno = []
    
    for elemento in lista:
        if elemento > n:
            lista_retorno.append(elemento) 
    return lista_retorno