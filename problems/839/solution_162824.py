def carros(pessoas, capacidade_1, capacidade_2=5):
    if pessoas//capacidade_2!=0:
         return pessoas//capacidade_2 + 1
    if pessoas < 5 or pessoas == 5:
            return pessoas//capacidade_1