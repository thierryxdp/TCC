# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao (meidas,H,L):
    [A,B,C]
	'''
	funcue recebe as dimensoes de um colchao e medidas de uma porta
	e retorna se é possivel ou nao passar por ela 
	lista,int,int ->bool
	'''
	result = bool
	if medidas [0] <= L and medias [1] <= H:
        result = True
    elif medidas [1] <= L and medias [0] <= H:
        result = True
    elif meidas [0] <= L and meidas [2] <= H:
          result = True
    else :
        result = False