def carros (p,c=5):
    '''define quantos carros podem ir 
    em uma viagem dado o numero p de pessoas
    e a capacidade c dos carros'''
    return (5+p)%(5+c)