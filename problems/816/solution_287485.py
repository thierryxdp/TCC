def maiores(numeros:lista[int],numero:int):
    """retorna os valores maiores que n em forma de lista"""
    for i in numeros:
        if i > numero:
            return list(i)