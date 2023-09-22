def inverte(frase):
    '''dada a frase, retorna a frase ba ordem inversa sem pontuação.
    str->str'''
    str.join(frase," ")
	return frase.replace("-"," ").replace(","," ").replace(":"," ").replace(";"," ").replace("."," ").replace("?"," ").replace("!"," ")
    inverte_frase=str.split(sem_pontuacao(frase))
    list.reverse (inverte_frase)
    return str.lower(str.join(' ',inverte_frase))