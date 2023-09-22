def retira_pontuacao (frase):
	""" dada uma frase, substirui os caracteres de pontuacao por espaco
    	:parametro frase: str
        :return: str"""
    frase = str. replace(frase, '-', ' ')
    frase = str. replace(frase, ',', ' ')
    frase = str. replace(frase, ':', ' ')
    frase = str. replace(frase, ';', ' ')
    frase = str. replace(frase, '.', ' ')
    frase = str. replace(frase, '!', ' ')
    frase = str. replace(frase, '?', ' ')
    frase = str. replace(frase, '...', ' ')
    	return frase