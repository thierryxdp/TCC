def qtd_divisores(n):
    '''função que dado um numero(n), retorna quantos divisores
    n tem;int->int'''
    divisor=1
    resp=[]
    for i in range((n-1),(n+1)):
        if (n%divisor)== 0:
            resp+=(n%divisor)
        divisor+=1
    return resp