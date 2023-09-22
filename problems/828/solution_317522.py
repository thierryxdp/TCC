def primo(n):
    '''Função que retorna true se um número é primo e false caso contrário, dado o número n;int->bool'''
    divisores=0
    nao_divisores=0
    for a in range(2,n):
        if n%a==0:
            divisores=divisores+1
        if n%a!=0:
            nao_divisores=nao_divisores+1
    return nao_divisores==len(range(2,n))