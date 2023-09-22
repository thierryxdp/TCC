def carros (pessoas, capacidade=5):
    'retorna a quantidade necessária de carros para comportar certo numero de pessoas'
    from math import ceil
    return ceil(pessoas/capacidade)