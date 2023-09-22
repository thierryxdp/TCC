def soma_h(n):
    '''função que calcula e retorna o valor de h com n termos onde n é inteiro e dado como entrada:int->float'''
    cont = 0 
    for n in range (1,n+1):
        cont += 1/n
    return round(cont,2)