def qtd_divisores(num):
    '''A funcao recebe um numero como entrada e retorna o numero de divisores que esse
numero possui int->int'''
    seq=list(range(1,num+1))
    divisores=[]
    for i in seq:
        if num%i==0:
            divisores.append(i)
    return len(divisores)