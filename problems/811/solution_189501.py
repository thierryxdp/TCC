# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(colchao,Hporta,Lporta):
	''' Função que calcula a possibilidade de passar o colchao na porta
list,int,int->bool'''
	colchao.sort
    if colchao[1] > Hporta and colchao[1] > Lporta:
        return False
    else:
        return True