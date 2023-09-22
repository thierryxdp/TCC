#importando o módulo math
import math

def carros(np, cv=5):
    '''calcula a quantidade de carros necessários para uma viagem, dado a quantidade de pessoas(np) e a capacidade do carro(cv) caso ela não seja a convencional(5); int, int -> int'''
    return math.ceil(np/cv)