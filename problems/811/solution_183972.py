# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas, H,L):
    [m1,m2,m3]=medidas
    if ((m2>H and m3>L) or (m2>L and m3>H) ) :
        return True
    elif ((m2>H and m3<=L) or (m2<=H and m3>L) or (m2>L and m3<=H) or (m2<=L and m3>L)):
        return (m1<L)
    elif (m2<=L and m3<=H) or (m2<=H and m3<=L):
        return True