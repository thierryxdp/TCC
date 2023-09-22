def filtra_pares(tupla):
    """função que recebe uma tupla com quatro elementos inteiros e retorna uma tupla contendo apenas os elementos pares da tupla original, na mesma ordem que se encontravam"""
    tupla=tupla[1],tupla[2],tupla[3],tupla[4]
    if tupla[1]%2==0:
        return tupla[1]
    if tupla[2]%2==0:
        return tupla[2]
    if tupla[3]%2==0:
        return tupla[3]
    if tupla[4]%2==0:
        return tupla[4]
    else:
        return tupla[]