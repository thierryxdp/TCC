def soma_h(termos):
    '''funcao que retorna o valor de h em uma funcao que tem n termos em que n e um inteiro
    int->float'''
    soma=0
    for i in termos:
        if i in soma:
            soma=soma+termos
    return round(soma,2)