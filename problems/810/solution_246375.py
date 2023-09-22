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
    frase = retira_pontuacao(frase)
    frase = list(str.split(frase,' '))
    list.reverse(frase)
    frasestring = str.join(' ',frase)
    return frasestring