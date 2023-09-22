import math
def carros(Npessoas, capacidade=5):
    '''calcula a quantidade de carros necessária baseado na capacidade do carro e o número de pessoas. se não for dado a capacidade, admite-se como 5.
       int, int -> float'''
    return abs(round((Npessoas/capacidade)+0.49999999999, 0))