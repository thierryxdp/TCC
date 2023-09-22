def qtd_divisores(num):
    """dado um número, a função retorna a quantidade de divisores que o número possui;
    int->int"""
    qtde=0
    for numero in range(num):
        if num=0:
            qtde=qtde
        elif num%numero==0:
            qtde=qtde+1
    return qtde+1