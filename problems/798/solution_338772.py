# Dado uma str retorna um dicionário onde cada palavra dessa str seja uma chave e tenha como valor o número de vezes que a palavra aparece nessa frase
# str-->dic
def freq_palavras(list):
	freq={}
	for x in list:
		if (x in freq):
			freq[x]+=1
		else:
			freq[x]=1
	return freq