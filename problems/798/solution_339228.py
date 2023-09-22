# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    palavras = frases.split()
    dicionario = {}
    count = 1
    vezes = 1
    for palavra in palavras:
        dicionario[count] = palavra
        count += 1
        for dicionario in dicionario:
            if dicionario[count] == dicionario[count]:
            	dicionario = dicionario + dicionario[count]
            else:
            	return dicionario
	return dicionario