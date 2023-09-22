def carros(pessoas,capacidade):
    ''' indica quantos carros são necessários para levar o total de pessoas para uma viagem
        int, int ---> int '''
    return int(pessoas//capacidade) + 1