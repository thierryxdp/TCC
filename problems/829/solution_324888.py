def soma_h(num):
    '''funcao que calcula e retorna o valor H com N termos'''
    cont = 0.0
    for i in range(1,num+1):
        cont+= 1/i
     return round(cont,2)