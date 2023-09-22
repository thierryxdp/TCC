def retira_pontuacao(frase):
    import string
    y=string.punctuation
    for x in y:
        frase = frase.replace(x,'')
    return(frase)
def inverte(frase):
	import string
    novafrase = retira_pontuacao(frase)
    minusculo = str.lower(novafrase)
    separa = minusculo.split()
    reverte = reversed(separa)
    juntastring = ' '.join(reverte)
    return juntastring