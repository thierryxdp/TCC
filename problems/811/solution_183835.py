# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    '''Função que dada as medidas de um colchão, retorna True se o mesmo da pra passar por uma porta dada
    suas medidas. Retorna False caso contrário.
    list, int, int -> boolean '''
    if medidas[0] <= H and medidas[1] <= L:
        return True
    elif medidas[0] <= L and medidas[1] <= H:
        return True
    elif medidas[2] <= H and medidas[1] <= L:
        return True
    elif medidas[0] <= L and medidas[2] <= H:
        return True
    return False