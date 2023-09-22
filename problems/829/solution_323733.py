def soma_h(termos):
    '''funcao que retorna o valor de h em uma funcao que tem n termos em que n e um inteiro
    int->float'''
    soma=0
    for i in range(1,1+termos):
        conta=1/i
        soma=soma+conta
    return round(soma,2)