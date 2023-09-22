def carros (pessoas):
    '''Calcula e retorna o numero de carros necessários para realizar uma viagem dado o número de pessoas 
    e considerando que pelas regras rodoviárias um veículo convencional tem a capacidade de transportar até 5 
    passageiros.
    int -> float'''
    
    if (pessoas//5) < (pessoas/5):
        return (pessoas//5)+1
    
    elif (pessoas//5) == (pessoas/5):
        return pessoas//5