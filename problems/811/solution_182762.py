# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    '''colchao recebe uma lista e dois num inteiros e
    devolve booleanas a funcao estabelece se o colcao
    entra ou nao na casa do joao
    list, int, int --> booleanas'''
    
    a = (medidas[1]>=H or medidas[2]>=L) and (medidas[1]>=L or medidas[2]>=H)
    
    return a