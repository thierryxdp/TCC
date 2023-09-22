# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,L,H):
    '''funcao que dados as medidas de um colchao e de uma porta determina se sera possivel passar com o colchao pela porta
    int,int,tupla->string'''
  
    if medidas[1]<L or medidas[1]<H:
        return True
    elif medidas[1]>L or medidas[1]>H:
        return False