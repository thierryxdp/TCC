def num_bombons(dinheiro,preco):
    '''calcula e retorna quantos bombons Pedrinho consegue comprar, dados o dinheiro que possui e o preço do bombom'''
    return dinheiro//preco

#Questão 2
def carros(g,p=4):
    '''Função que calcula e retorna o numero de carros com capacidade para 'p' pessoas, necessario para transportar o grupo com 'g' passageiros'''
    
    g= int(g)
    p= int (p)
    c = g/p
    
    if (g==0):
        return 0
    if (g<p):
        return 1
    elif (g>p):
        import math 
        return math.ceil(c)