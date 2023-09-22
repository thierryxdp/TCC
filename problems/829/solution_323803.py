def soma_h(N):
    ''' a funcao retorna o valor de H com n termos
    int-> int'''
    soma=0
    for i in range(1, 1+N):
        calculo=1/i
        soma=soma+calculo
    return round(soma, 2)