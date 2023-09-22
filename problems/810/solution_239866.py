def retira_pontuacao(frase):
	frase=frase.replace('.',' ')
    frase=frase.replace('-',' ')
    frase=frase.replace(',',' ')
    frase=frase.replace(';',' ')
    frase=frase.replace(':',' ')
    frase=frase.replace('!',' ')
    frase=frase.replace('?',' ')
    frase=frase.replace('...',' ')
    return frase
def inverte(frase):
    frase=retira_pontuacao(frase)
    frase= frase.split(' ')
    frase=frase[-1::-1]
    frase= str.join(' ',frase)
    frase= str.lower(frase)
    frase= str.strip(frase)
    frase= frase.replace('  ',' ')
    return frase