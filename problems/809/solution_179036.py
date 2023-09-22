# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(l1, l2):
    '''Esta e a funcao que dadas duas listas l1 e l2
    de tamanho 3, geram uma lista l3 que é formada 
    intercalando elementos de l1 e l2'''
    i=len(l1)
	j=len(l2)
	l3=l1[0:i+1:2]+l2[0:j+1:2]
	l4= l1[1:i+1:2]+l2[1:j+1:2]
	l5=l3+l4
	l5.sort()
	return l5