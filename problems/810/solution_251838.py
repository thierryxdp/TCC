def sempontuacao(frase):
	'''a frase sem pontuac~ao
	str -> str'''
	sem_pontos = str.replace(str.replace(str.replace(frase,","," "),"."," "),"..."," ")
	sem_pontos2= str.replace(str.replace(str.replace(sem_pontos,"!"," "),"?"," "),";"," ")
	return str.replace(str.replace(sem_pontos2, ":", " "), "-"," ")

def inverte(frase):
    frase = frase.lower()
    frase = sempontuacao(frase)
    frase = frase.split()
    return str.join(' ', frase[::-1])