def carros (p,c=5):
    """calcula a quantidade de carros de 5 lugares necessária para comportar um número p de pessoas"""
    return max(p/c)