# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    '''a função colchao dado a lista "medidas" 
    que contem as dimensões do colchao e H e L 
    a altura e a largura da porta respectivamente
    retorna True se o colchao passa pela porta e False
    se não passar (lista,int,int->booleano)
    '''
    if medidas[1] <= H:
        return True
    elif medidas[2] <= L:
        return True
    else:
        return False