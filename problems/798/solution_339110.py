# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    palavras = frases.split()
    dicionario = {}

    for palavra in frases:
    	if palavra in frases:
        	count = 1
        	if palavra in dicionario:
          	count = int(dicionario[palavra].split(' ')[-1]) + 1;
        	dicionario[palavra] = palavra + " " + str(count)
    return dicionario