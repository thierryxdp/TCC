'''funçao que retorna se um colchao passa ou nao pela porta'''
# Escolha nomes elucidativos para suas variáveis
def colchao(medida,H,L):
    A=medida[0]
    B=medida[1]
    C=medida[2]
    
    if (A<=H) and (B<=L):
        return True
    if (A<=L) and (C<=H):
        return True
    if (A<=L) and (B<=H):
        return True
    else if:
        retur False