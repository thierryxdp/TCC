def qtd_divisores(n):
    '''Função retorna o número de divisores de certo número
       int -->int'''
    seq = list(range(1,n+1))
    divisores=[]
    for i in seq:
        if n%i==0:
            divisores.append(i)
    return len(divisores)