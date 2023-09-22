# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    """ função que retorna a possibilidade de passar um colchão por uma porta (True), ou a impossibilidade (false)
    dados uma lista contendo as medidas do colchão, 'H' para a altura da porta e 'L' para a largura.
    
    Parâmetros:
    	medidas
        	Lista com as dimensões do colchão
        H,L:
        	Inteiros que representam a altura e largura da porta, respectivamente
            
     Retorna:
     	Um booleano, 'True' apara afirmação que o colchão passa, 'False' para a negativa dessa

	"""
    
    if H>= medidas[0] and L>= medidas[1]:
        return True

    elif H>= medidas[1] and L>= medidas[0]:
        return True
    else:
        return False