def divisores (num):
    """Função que dado um numero de entrada, retorne quantos divisores esse numero tem; int->int"""
    lista = []
    i = 1 
    while i < num + 1:
        if num % i == 0:
            list.append(lista,i)
        i = i + 1 
    return len(lista)