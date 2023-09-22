"""
Nesta função, a string é transformada em uma list e após isso
cada item da lista é adicionado ao dict criado e usa-se o str.count
para ser o valor de cada chave. 
str -> dict
"""
def freq_palavras(frases):
    freq = {}
	frase_list = frases.split(' ')
    for i in range(len(frase_list)):
        freq[frase_list[i]] = frase_list.count(frase_list[i])
    return freq