def carros(num_pessoas,num_vagas=5):
    """ retorna o numero exato de carros necessarios
    para realizar uma viagem de amigos, dados o numero
    de pessoas "num_pessoas" e a capacidade de pessoas
    dentro do carro "num_vagas". 
    se a capacidade do carro nao for informada sera 
    considerado 5 como dado de entrada
    int, int -> int"""
    return math.ceil(num_pessoas/num_vagas)