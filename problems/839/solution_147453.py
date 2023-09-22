import math

def carros(p,c=5):
    '''calcula a quantidade necessária de carros com capacidade c, caso não seja informado será considerado um carro com capacidade convencional de 5 lugares, para um certo números p de pessoas;
    	int,int -> int'''
    return math.ceil(p/c)