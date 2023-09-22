def qtd_divisores(num):
    """dado um número, a função retorna a quantidade de divisores que o número possui;
    int->int"""
    qtde=0
    for numero in range(num):
        if numero%num==0:
        qtde=qtde+1
    return qtde