# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    """A função retorna se o colchão de dimensões (medidas), passa pela porta de altura H e largura L.
    list,int,int-->bool"""
    a,b,c = medidas
    if b<=H:
        d=True
    elif c<=L:
        d=True
    else:
        d=False
    return d