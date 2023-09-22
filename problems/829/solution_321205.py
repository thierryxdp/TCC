def soma_h(numero):
    '''Fun;'ao que calcula o valor da soma H com N termos; 
    int->float'''
    soma=0
    for i in range (1,numero+1):
        i=1/i
        soma=soma+i
    return round(soma,2)