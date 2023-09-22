def soma_h(numero):
    '''função que retorna o valor de H com
    N termos'''
    
    cont = 0.0
    for i in range(1,numero+1) :
        cont += 1/i
    return round(cont,2)