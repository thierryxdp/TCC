from math import floor
def hashtag(s):
#Recebe uma string e retorna sua concatenação
# com as #
# str-> str
	tamanhoDaPalavra = len(s)
	meioDaPalavra = tamanhoDaPalavra/2
    meioImparDaPalavra = floor(meioDaPalavra)
	if tamanhoDaPalavra%2 == 0:
        return "#" + s[0: meioDaPalavra + 1] + "#" + s[meioDaPalavra+1:tamanhoDaPalavra+1] + "#" 
    else:
        return "#" + s[0: meioImparDaPalavra + 1] + "#" + s[meioImparDaPalavra + 1: tamanhoDaPalavra+1] + "#"