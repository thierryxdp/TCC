# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
'''Separa a string em uma lista onde cada elemento é uma palavra 
	da string original. Depois, contabiliza o número de palavras iguais
    da string em forma de dicionário.
'''
def separa_palavras(frases):
    return str.split(frases)
def freq_palavras(frases):
    d = {}
    for palavras in separa_palavras(frases):
        d[palavras] = dict.get(d, palavras, 0) + 1
	return d