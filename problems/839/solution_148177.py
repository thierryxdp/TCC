def carros(g,p=4):
    """Função que calcula e retorna o numero de carros com capacidade para 'p' pessoas, necessario para transportar o grupo com 'g' passageiros"""
    if g<4: 
        return 1
    else:
        return g//p