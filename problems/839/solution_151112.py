def carros(pessoas,lugares=5):
    '''calcula e retorna a quantidade de carros necessarios para levar x pessoas, 5 é o valor default para os lugares no carro;
    int,int->int'''
    import math
    return math.ceil(pessoas/lugares)