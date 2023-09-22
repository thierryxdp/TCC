import math
def carros(p,c=5):
    """Calcula e retorna o numero exato de carros necessarios para a 
    realizacao de uma viagem de p pessoas transportadas em carros com
    capacidade para c pessoas;
    int,int->int"""
    return math.ceil(p/c)