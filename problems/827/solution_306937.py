def qtd_divisores(numero):
    """funcao que conta quantos divisores um numero dado de entrada tem. int->int"""
    lista_divisores=[numero]
    for i in range(1,numero//2+1):
        if numero%i==0:
            list.append(lista_divisores,i)
    return len(lista_divisores)