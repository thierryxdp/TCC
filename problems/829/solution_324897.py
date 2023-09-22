def soma_h(num):
    '''Calcula e retorna o valor H com N termos, onde N 
    é inteiro e dado com entrada'''
    '''int->'''
    cont=0.0
    for i in range(1,num+1):
        cont+=1/i
    return round(cont,2)