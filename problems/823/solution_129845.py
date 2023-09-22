from random import randint
def faltante(x):
    #Será feita uma lista de 1 a N de peças
    l = [*range(1, n+1)]
    #E depois será retirado uma peça aleatória do quebra-cabeça
    while len(l) == n:
        #já que a lista vai de 1 até n, seu posicionamento vai de 0 até n-1, já no python a posição inicial é o 0
        sumiu = randint(0, n-1)
        #O número aleatório é retirado da lista
        del(l[sumiu])
        #O posicionamento é tratado para se referir à peça
        faltante = sumiu + 1
        #O resultado é impresso
    return faltante