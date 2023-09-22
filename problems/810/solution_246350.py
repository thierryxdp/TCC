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
    lista = str.split(frase,' ')
    frase = list.reverse(frase)
    return frase