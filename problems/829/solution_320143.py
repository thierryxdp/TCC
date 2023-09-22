def soma_h(n):
    '''funcao que calcula e retorna o valor de H com N termos, com N inteiro
    int->float'''
    soma=0
    for h in range(1,n+1):
        soma+=(1/(h))
        return round (soma,2)