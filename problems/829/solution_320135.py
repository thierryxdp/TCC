def soma_h(n):
    '''funcao que calcula a soma, none->float'''
    soma=0
    for h in range(n):
        soma+=(1/(h+1))
        return round(soma,2)