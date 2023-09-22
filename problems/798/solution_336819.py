''' A função recebe uma string e retorna um dicionário onde cada palavra dessa string seja uma chave
e  tenha como valor o número de vezes que a palavra aparece.
srt -> dic'''
def freq_palavras(frases):
    a=frases.split()
   	#b=len(a)
    c={}
    for item in a:
        b=a[item]
        d=a.count(b)
        #c.append(d)
        c[a[item]]=d
	return c