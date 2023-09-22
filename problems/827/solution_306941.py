def qtd_divisores(numero):
    """funcao que conta quantos divisores um numero dado de entrada tem. int->int"""
    lista_divisores=[numero]
    if numero>0:
        for i in range(1,numero):
            if numero%i==0:
                list.append(lista_divisores,i)
        return len(lista_divisores)
    else:
        return 0