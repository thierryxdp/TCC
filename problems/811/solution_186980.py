def piramide_num(num1, num2):
    """Insira dois números inteiros. A função devolve uma lista pirâmide.
       int, int --> list"""

    lista1 = [num1]

    if num1 > num2:
        return list(range(num1, num2, -1)) + list(range(num2, num1)) + lista1
    elif num1 < num2:
        return list(range(num1, num2)) + list(range(num2, num1, -1)) + lista1
    else:
        return lista1