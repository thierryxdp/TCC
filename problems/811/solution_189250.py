# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    '''Função que recebe como entrada uma lista contendo as medidas do colchão de joão, a altura H
    e a largura L da porta que esse colchão irá passar. A função retorna True caso o colchão
    passe pelas portas ou False caso contrário; lista,int,int->bool'''
    if medidas[1]<=H or medidas[2]<=L:
        return True
    else:
        return False