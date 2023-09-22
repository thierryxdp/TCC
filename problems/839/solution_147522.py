def carros(pessoas, capacidade=5):
        'retorna a quantidade necessária de carros paa comportar certo numero de pessoas'
         from math import ceil
        return ceil(pessoas/capacidade)