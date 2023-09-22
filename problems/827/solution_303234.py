def qtd_divisores(n):
    '''Função que retorna a quantidade de divisores que um número tem
       int->int'''
    a=0
    b=[]
    for x in range(1,n+1):
        if n%x==0:
            b.append(x)
    return len(b)