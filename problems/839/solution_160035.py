def carros(pessoas,vagas=5):
    '''Calcula e retorna quantos carros são necessários para uma viagem dado o número de pessoas e as vagas disponíveis no carro;
    int, int -> int'''
    return round(pessoas/vagas)