# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas=list,H,L):
    """Cálculo de uma função que tem como objetivo calcular se, a partir das dimensões
    do colção, este passa por uma porta com altura H e largura L.
    
    Parameters:
    medidas
    
    """
    medidas = [A,B,C]
    if C<= max(H,L) and B<= max(H,L):
        return True
    else:
        return False