def carros(pessoas,capacidade=5):
    '''funcao que retorna quantos carros sao necessarios, dado o numero de pessoas viajando
    int, int -> int'''
    numero = pessoas%capacidade
    total = pessoas//capacidade
    if numero > 0:
        total += 1
    else:
        total = total
    return total