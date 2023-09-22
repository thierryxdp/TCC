# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    palavras = frases.split()
    dicionario = {}
    for palavra in frases:
    	dicionario = dicionario + (dicionario[palavra], )
    return dicionario