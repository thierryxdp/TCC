def soma_h(n): 
    '''funçao que retorna o soma de 1 divido pelo intervalo de 1 a n de entrada''' 
    '''int->float'''
    total=0
    for x in range(1,n+1):
        soma=(1/x) 
        total+=soma
    return round(total,2)