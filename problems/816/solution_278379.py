def maiores(lista,n):
    """
    Retorna os numeros maiores que o indicado presentes em uma lista
    Parametros:
    	lista -> list
        lista de inteiros
        n -> int
        numero a ser comparado
    Returns:
    	list
        lista de numeros maiores que n
    """
    list.append(lista,n)
    list.sort(lista)
    maiores=lista[list.index(lista,n)+1,]
    return maiores