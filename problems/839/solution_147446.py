from math import ceil
def carros(p,cc=5):
    '''Calcula e retorna o número de carros neccessarios 
    para acomodar n pessoas, dados o número de pessoas p 
    e se diferente de 5 a capacidade do carro cc
    	int,int -> int'''
    return ceil(p/cc)