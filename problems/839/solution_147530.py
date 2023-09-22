def carros (pessoas, capacidade=5):
    '''Calcula a quantidade de carras necessários para se fazer uma viagem.
    int,int -> int'''
    return ceil(pessoas/capacidade)