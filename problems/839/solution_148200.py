def carros(g,p=4):
    """Função que calcula e retorna o numero de carros com capacidade para 'p' pessoas, necessario para transportar o grupo com 'g' passageiros"""
    if (g==0):
        return 0
    elif (g>p):
        if float(g//p):
            return int((g//p) + 1)
        elif int(g//p):
            return g//p