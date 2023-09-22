from math import ceil

def carros(p,c=5):
    """funçao que recebe como parametros a quantidade p de pessoas e a
    capacidade c dos veiculos utilizados e retorna o numero extato de 
    carros necessarios para a viagem;
    int, int -> int
    """
    return ceil(p/c)