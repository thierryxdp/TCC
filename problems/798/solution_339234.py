# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    palavras = frases.split()
    dicionario = {}
    count = 1
    vezes = 1
    count2 = 0
    vezes2 = 1
    for palavra in palavras:
        dicionario[count] = palavra
        count += 1
        for dicionario in dicionario:
            if dicionario[count2] == dicionario[vezes2]:
            	dicionario = dicionario + dicionario
            else:
            	return dicionario
	return dicionario