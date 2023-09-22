import math
def carros(p,c=5):
   '''Função que dada quantidade de pessoas p, retorna número de carros exatos necessários para a viagem;
caso o carro/veículo possua maior ou menor quantidade, informar entrada;
int, int -> float'''
   return math.ceil(p/c)