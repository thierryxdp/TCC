# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(a):
    resultado = a.split()
    dicio = {}
    for i in resultado:
        dicio[i] = dicio[i] + 1 if i in alfabetos else 1
	return dicio