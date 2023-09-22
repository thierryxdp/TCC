# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    """A função retorna se o colchão passa pela porta dadas as medidas 
       do colchao e a altura e largura da porta;
       list,int,int->bool
       Parâmetros:
       medidas: medidas do colchao
       H: altura da porta
       L: largura da porta
    """
    [a,b,c] = medidas
    if c<=l or b<=h:
        return True
    else:
        return False