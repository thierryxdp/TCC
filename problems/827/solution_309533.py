def qtd_divisores(n):
    '''função que dado um numero(n), retorna quantos divisores
    n tem;int->int'''
    divisor=1
    resp=0
    for i in range((n-2),n):
        if (n%divisor)== 0:
            resp+=(n%divisor)
        divisor+=1
    return resp