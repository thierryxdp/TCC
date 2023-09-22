def colchao(medidas,h,l):
# Coloque um comentário dizendo o que a função faz
'''funçao que recebe o tamanho de um colchao e de uma porta e retorna se o colchao consegue passar pela porta;
int,int,int,int,int,int->bol'''
# Escolha nomes elucidativos para suas variáveis
	espessura , largura, altura = medidas
	if largura <h and espessura < l :
    return True
	else:
    return False