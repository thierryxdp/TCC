def concatenacao(a, b):
    '''função que retorna a concatetação das strings A e B
    no formato ABBA
    entrada:str
    saída:str'''
    c = (a,b)
    d = c[0] + c[1] + c[-1] + c[-2]
    print ('d')