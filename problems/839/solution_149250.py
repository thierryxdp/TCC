def carros (n,c=5):
    '''função que retorna a quantidade de carros para fazer uma viagem, dados o número de pessoas (n) e a capacidade máxima por passageiros (c)'''
    return max (round (n/c))