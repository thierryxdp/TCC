def carros(p,c=5):
    ''' Retorna o número necessario de carros para uma viagem, dados o número de pessoas p e a capacidade dos carros c. int, int -> int'''
    return (ceil(p//c))