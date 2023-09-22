''' A função recebe uma string e retorna um dicionário onde cada palavra dessa string seja uma chave
e  tenha como valor o número de vezes que a palavra aparece.
srt -> dic'''
def freq_palavras(frases):
    a=frases.split()
   	#b=len(a)
    c={}
    for item in a:
        d=a.count(item)
        #c.append(d)
        c[item]=d
	return c