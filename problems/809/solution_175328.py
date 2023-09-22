def intercala(lista1, lista2):
    """Retorna a lista 1 e a lista 2 intercalando entre elas
    int, int -> int"""
    return lista1[0:1]+lista2[0:1]+lista1[1:2]+lista2[1:2]+lista1[2:3]+lista2[2:3]