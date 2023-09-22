def sem_pontuacao(frase):
    '''dada a frase, inverte a ordem das palavras, retira as letras maiúculas e a pontuação.
    str->str'''
	str.join(frase," ")
	return frase.replace("-", " ").replace(",", " ").replace(":", " ").replace(";", " ").replace(".", " ").replace("?", " ").replace("!", " ")
def inverte(frase):
    '''dada a frase, retorna a frase invertida sem letras maiúsculas.
    str -> str'''
    nova_frase=str.split(sem_pontuacao(frase))
    list.reverse (nova_frase)
    return str.lower(str.join(' ', nova_frase))