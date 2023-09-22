def soma_h(num):
    '''Recebe um numero inteiro, calcula e retorna o valor H com
    N termos;
    int->float'''
    
    contador=0
    for i in range(1,num+1):
        contador+=1/i
    return round(contador,2)