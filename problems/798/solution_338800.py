# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(a):
    resultado = a.split()
    dicio = {}
    for i in enumerate(resultado):
    	dicio = dicio + resultado[i]
	return dicio