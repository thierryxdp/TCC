# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    """ Verifica se o colchao com as dimenões fornecidas passa pela porta.
    	entrada: lista e 2 int -> saida:boleao, retorna true caso o colchão passe."""
	if((medidas[0]or medidas[1]or medidas[2])< H):
        return bool("True")
    
    else:
        return (medidas[0]*medidas[1]*medidas[2]) <= (H*L)