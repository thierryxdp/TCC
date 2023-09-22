def qtd_divisores(numero):
    '''funcao que conta quantos divisores um numero tem;
    int->list'''
    soma=0
    div=range(1,n+1)
    if numero<0:
        return 0
    for f in div:
        if numero%f==0:
            soma=soma+1
    return soma