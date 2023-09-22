def carros(p:int,a:int):
    
    '''calcula quntos carros são necessários, sendo p o número
    de passageiros e a o número de assentos'''
    
    return((p//a) +(1 if p/a % int(p/a) else 0))