def qtd_divisores(n:int)->int:
    '''Função que conta quantos divisores um dado número inteiro tem.'''
    divisores=list()
    for num in range(1,n+1):
        if n%num==0:
            divisores.append(num)
    return len(divisores)