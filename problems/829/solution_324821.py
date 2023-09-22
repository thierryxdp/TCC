def soma_h(num):
    '''função que calcula e retorna o valor h com n termos'''
    cont = 0.0
    for i in range(1,num+1):
        cont+= 1/i
    return round (cont,2)