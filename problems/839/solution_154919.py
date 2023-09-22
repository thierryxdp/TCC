def carros(p:int,a=5)-> int:
    
    '''calcula quntos carros são necessários, sendo p o número
    de passageiros e a o número de assentos'''
    
    from math import ceil

    return ceil (p/a)