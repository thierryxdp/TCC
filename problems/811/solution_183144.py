# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(tuple,H,L):
    """Para saber se o colchão passa pela porta, digite;
    tupla, int, int-> Booleano"""
    X= int(tuple[1])
    if H>=X:
    	return True
    else:
       	return False