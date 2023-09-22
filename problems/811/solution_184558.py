# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    """Cálculo de uma função que tem como objetivo calcular se, a partir das dimensões
    do colchão, este passa por uma porta com altura H e largura L.
    
    Parameters:
    medidas: corresponde as dimensões do colchão
    H: corresponde a altura da porta
    L: corresponde a largura da porta
    
    Returns: 
    Retorna true se as medidas do colchão passam pela porta e false se não passam dado que:
    list, float, float -> bool
    """
    if medidas[1]<=H:
        return True
    else:
        return False