# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
# A->altura,B->base,C->largura    
    A,B,C=medidas
    A=int(A)
    B=int(B)
    C=int(C)
#caso1:colchao deitado    
    if (A<=H or A<=L)and(B<=H or B<=L):
        return True
        '''colchão '''
        if (C<=H and A<=L):
            return True
        else:
            return False
    else:
        return False