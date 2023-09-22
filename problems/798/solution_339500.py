# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    d = {}
    f = frases.split(' ')
    j = []
    for i in f:
        if i not in j:
        	d[i] = f.count(i)
		j.append(i)
    return d