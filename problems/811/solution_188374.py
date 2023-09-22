# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas, H, L):
    """Função que recebe uma lista contendo as medidas de um colchão e dois números inteiros que representam as medidas de uma porta
	e retorna True se o colchão passa pela porta ou False se não.
	list, int, int -> bool"""
    
    a = medidas[0]
    b = medidas[1]
    c = medidas[2]
    
    if H >= b:
        return True
    else:
        return False