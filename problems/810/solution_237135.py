def retira_pontuacao(frase):
	frase = frase.replace('-', ' ').replace(',', ' ').replace(':', ' ').replace(';', ' ').replace('!', ' ').replace('?', ' ').replace('...', ' ').replace('.', ' ')
    return frase

def inverte(frase):
    frase = retira_pontuacao(frase)
    lista = frase.split(' ')
    lista.reverse()
    lista.remove('')
    frase = str.join(' ', lista)
    return frase