def carros(num_pessoas, cap_carro=5):
    '''Calcula o número de carros necessários para uma viagem,
    dado a quantidade de pessoas totais na viagem e a capacidade
    que cada carro comporta.
    OBS: caso não seja informada a capacidade do veículo, por padrão
    a função definirá a capacidade para 5, seguindo regras rodoviárias.'''
    
    import math
    
    return math.ceil(num_pessoas / cap_carro)