def carros(pessoas,assentos=5):
    """funcao que calcula a quantidade de carros necessarios para uma viagem"""
    x=pessoas
    y=assentos
    if x%y==0:
     return x/y
    else:
     return x//y+1