'''funçao que retorna se um colchao passa ou nao pela porta'''
# Escolha nomes elucidativos para suas variáveis
def colchao(medida,H,L):
    A=medida[0]
    B=medida[1]
    C=medida[2]
    
    if (A>H) and (B>L):
        return False
    if (A<H) and (B<L):
        return True