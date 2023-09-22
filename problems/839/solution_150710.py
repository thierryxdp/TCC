import math
def carros(pessoas,capacidade=5):
    '''calcula a quantidade de veiculos necessários para uma viagem, dados o número de pessoas. caso os veículos considerados sejam de capacidades nao convencionis,também será dada a sua capacidade.'''
    return math.ceil(pessoas/capacidade)