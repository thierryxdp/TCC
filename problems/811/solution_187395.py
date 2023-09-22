# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    '''
        dadas a dimensoes de um colchao e a largura e a altura da porta por
        onde deve passar o colchao, retorna True se o colchao passa pela porta
        ou False caso o colchao nao passe
        entrata: lista, inteiro, inteiro
        saida: booleano
    '''
    A, B, C = medidas
    lmin=min(A, B, C)
    lmax=max(A, B, C)
    if (lmin==A and lmax==C) or (lmin==C and lmax==A):
        lmed=B
    if (lmin==B and lmax==C) or (lmin==C and lmax==B):
        lmed=A
    if (lmin==A and lmax==B) or (lmin==B and lmax==A):
        lmed=C
    if (lmin<=L and lmed<=H) or (lmin<=H and lmed<=L):
        return True
    else:
        return False