def carros(p,c=5):
    '''retorna o número de carros necessários para que p passageiros sejam 
    acomodados em carros com capacidades convencionais, 5 assentos; int,int->
    int'''
    return (p+c-1//c)