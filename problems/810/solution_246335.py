def retira_pontuacao(frase):
	frase = frase.replace('-',' ')
    frase = frase.replace('.',' ')
    frase = frase.replace(',',' ')
    frase = frase.replace(':',' ')
    frase = frase.replace(';',' ')
    frase = frase.replace('?',' ')
    frase = frase.replace('!',' ')
    return frase
def inverte(frase):
    return frase.join(frase.reverse(frase.split(retira_pontuacao(frase),' ')))