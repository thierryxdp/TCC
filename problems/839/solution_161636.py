def carros (p,c):
    """Calcula o numero de carros com capacidade c dado o numero p de passageiros"""
    if c=5 and p<=5:
        return 1
    else c=5 and p>5:
         return p//c
    else c!=5:
        return p//c + 1