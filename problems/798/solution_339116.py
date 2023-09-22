# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    palavras = frases.split()
    dicionario = {}
    for palavra in frases:
    	if palavra in palavras:
        	count = 1
            dicionario = dicionario + int.dicionario[palavra]
    return dicionario