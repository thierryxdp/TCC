def qtd_divisores(x):
    """essa função recebe um número qualquer e retorna
    o total de divisores que esse número possui;
    int->int"""
    num=0
    if x < 0:
        return 0
    for i in range(1,int(x/2+1)):
        if x % i == 0:
            num += 1
            return num += 1