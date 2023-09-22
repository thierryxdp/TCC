import math
def carros(pessoas,lugares=5): 
    car=math.ceil(pessoas/lugares)
    ''' funcao que calcula pessoas e lugares para 
    definir quantos carros serao necessarios 
    int, int -> int''' 
    return car