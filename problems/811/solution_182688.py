# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    """Função que define se é posível passar um colchão de dimensões A,B e C dadas 
    na lista medidas, por uma porta de altura H e largura L,sendo que um dos lados 
    do colchão é paralelo ao chão
    list,int,int-->bool"""
    A,B,C=medidas
    maiorporta=max(H,L)
    menorporta=min(H,L)
    if((A>maiorporta and B>maiorporta)or(A>maiorporta and C>maiorporta)or(B>maiorporta and C>maiorporta)):
        return False
    elif(min(medidas)>menorporta):
        return False
    else:
        return True