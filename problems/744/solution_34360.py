from math import floor
def hashtag(s):
#Recebe uma string e retorna sua concatenação
# com as #
# str-> str
	tamanhoDaPalavra = len(s)
	meioDaPalavra = tamanhoDaPalavra/2
    meioImparDaPalavra = floor(meioDaPalavra)
	if tamanhoDaPalavra%2 == 0:
        return "#" + s[0: meioDaPalavra] + "#" + s[meioDaPalavra:tamanhoDaPalavra] + "#" 
    else:
        return "#" + s[0: meioImparDaPalavra] + "#" + s[meioImparDaPalavra: tamanhoDaPalavra] + "#"