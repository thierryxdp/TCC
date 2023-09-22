def qtd_divisores(numero):
    """funcao que conta quantos divisores um numero dado de entrada tem. int->int"""
    lista_divisores=[numero]
    for i in range(1,numero):
        if numero%i==0:
            lista_divisores.append(i)
    return len(lista_divisores)