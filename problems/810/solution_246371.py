def retira_pontuacao(frase):
	frase = frase.replace('-',' ')
    frase = frase.replace('.',' ')
    frase = frase.replace(',',' ')
    frase = frase.replace(':',' ')
    frase = frase.replace(';',' ')
    frase = frase.replace('?',' ')
    frase = frase.replace('!',' ')
    return frase
def invertelista(frase):
    frase = retira_pontuacao(frase)
    frase = list(str.split(frase,' '))
    list.reverse(frase)
    return frase
def inverte(frase):
    return str.join(inverstelista(frase))