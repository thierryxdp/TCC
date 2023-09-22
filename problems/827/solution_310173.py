def qtd_divisores(n):
    '''retorna quantos divisores um número inteiro tem;
int->int'''

    divisores=[]
    d=1

    for valores in range(n+1):
        if n%d==0:
            list.append(divisores,d)
        d=d+1

    return len(divisores)