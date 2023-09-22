def concatenacao(a, b):
    '''função que retorna a concatetação das strings A e B
    no formato ABBA
    entrada:str
    saída:str'''
    c = (a,b)
    d = (a,b) + c[1] + c[0]
    print (d)