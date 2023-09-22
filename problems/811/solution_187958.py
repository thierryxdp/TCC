# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    '''função que retorna a possibilidade de um colchão
    passar por uma porta 
    valor de entrada: dimensões do colchao como medidas(list),
    int para altura H e int para largura L
    valor de saída: bool'''
    if medidas[0] and medidas[1] <=max(H,L):
        return True
    elif medidas[0] and medidas[2] <=max(H,L):
        return True
    elif medidas[1] and medidas[2] <=max(H,L):
        return True
    else:
        return False