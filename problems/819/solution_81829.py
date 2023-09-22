def filtraMultiplos(lista, n):
    """
    Essa função recebe uma lista de números e um número n, 
    e retorna uma lista com os múltiplos de n;
    list, int -> list
    """
    lista_resultado = []
    for x in lista:
        if x % n == 0:
            lista_resultado.append(x)
   	return lista_resultado