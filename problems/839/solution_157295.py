def carros(pessoas=10, capacidade=5):
    """ A função calcula a quantidade de carros necessários para um viagem  
    porpocional a uma determinada quantidade de pessoas, sabe-se que 
    cada veículo convecional pode transportar até 5 pessoas. Os veículos não 
    convencionais """
    return math.ceil(pessoas//capacidade)