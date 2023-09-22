import math
def carros(p,l=5):
    '''calcula e retorna o numero exato de carros necessarios para uma viagem, considerando que seja dado como entrada o numero de pessoas.
Caso os veıculos considerados sejam de capacidades nao convencionais, seram dados como entrada
o numero de lugares do veiculo, considerando que todos os veiculos sao iguais. int,int-->int'''
    return math.ceil(p/l)