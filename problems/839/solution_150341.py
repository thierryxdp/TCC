def carros (pessoas,capacidade=5):
    '''Calcula e retorna o numero de carros necessários para realizar uma viagem dado o número de pessoas e 
    a capacidade do carro. Considerando que caso a capacidade do carro não seja dada, pelas regras rodoviárias um veículo convencional tem a capacidade de transportar até 5 
    passageiros,.
    int -> float'''
    
    if (pessoas//capacidade) < (pessoas/capacidade):
        return (pessoas//capacidade)+1
    
    elif (pessoas//capacidade) == (pessoas/capacidade):
        return pessoas//capacidade