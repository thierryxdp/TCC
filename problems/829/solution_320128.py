def soma_h(n):
    '''funcao que calcula a soma, none->float'''
    soma=0
    for h in range(1,n+1):
        soma+=(1/(h))
        return round(soma,2)