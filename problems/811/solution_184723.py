# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    '''Funcao que retorna True ou False caso um colchão consiga passar, ou não
        por uma porta de dimensões H e L, dado as mesmas e a lista com dimensões
        do colchão D.
        lista(float,float,float) -> int,int'''
    

    if medidas[1] < H:
        return True
    elif medidas[-1] <= H:
        return True
    else:
        return False