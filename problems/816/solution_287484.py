def maiores(numeros:lista,numero):
    """retorna os valores maiores que n em forma de lista"""
    for i in numeros:
        if i > numero:
            return list(i)