def qtd_divisores(n):
    '''função que dado um numero(n), retorna quantos divisores
    n tem;int->int'''
    resp=[]
    for i in range(2,n//2+1):
        if n % i == 0:
            resp+=str(i)
        if 
    return len(resp)