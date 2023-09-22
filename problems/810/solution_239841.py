def retira_pontuacao(frase):
	'''substitui pontuacao da string por espaço.
    str -> str'''
    frase_nova = frase.replace('!', ' ')
    frase_nova = frase.replace('?', ' ')
    frase_nova = frase.replace(',', ' ')
    frase_nova = frase.replace('.', ' ')
    frase_nova = frase.replace(';', ' ')
    frase_nova = frase.replace(':', ' ')
    frase_nova = frase.replace('-', ' ')
    return frase_nova
def inverte(frase):
    retira_pontuacao(frase)
    return ' '.join(frase_nova.split()[::-1])