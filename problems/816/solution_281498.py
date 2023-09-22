def maiores(lista,n):
    """Retorna uma lista em ordem crescente contendo todos os números da lista
    original que sejam maiores que n. 
list, int -> list"""
    lista2 = [x for x in lista if x > n]
    list.sort(lista2)
    return lista2 

# Casos de teste:
# maiores([2,6,3,9,8],2) == [3, 6, 8, 9]
# maiores([3,11,7,9,5],6) == [7, 9, 11]
# maiores([102,34,27,66],30) == [34, 66, 102]