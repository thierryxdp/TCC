from math import ceil
def carros(pessoas, vagas=5):
    '''Calcula e retorna a qntd de carros necessarios para uma viagem com
    N pessoas;
    int, int -> int '''
    qntd_carros = pessoas/vagas
    return ceil(qntd_carros)