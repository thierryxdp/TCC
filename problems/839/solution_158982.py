def carros(pessoas,capacidade=5):
    ''' indica quantos carros são necessários para levar o total de pessoas para uma viagem
        int, int ---> int '''
    if (pessoas % capacidade) < 5 and =! 0:
        return (pessoas // capacidade) + 1