# Questão 6
def soma_h (N):
    ''' Função harmônica que recebe n termos e calcula a função harmoncia desses n termos'''

    fator_mult = 0
	x = 1
    while x <= N:
        fator_mult += 1/N
        x += 1
    return round (fator_mult,2)