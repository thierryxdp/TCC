def carros(g,p=4):
    """Função que calcula e retorna o numero de carros com capacidade para 'p' pessoas, necessario para transportar o grupo com 'g' passageiros"""
    g= int(g)
    p= int (p)
    c = g//p
    
    if (g==0):
        return 0
    if (g<p):
        return 1
    elif:
        if int(c): 
           return c
        elif float(c):
           return c + 1