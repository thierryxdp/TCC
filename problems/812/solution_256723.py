def retira_pontuação(frase):
    '''retira e retorna a pontuação da frase
    str->str'''
    for i in range(len(frase)):
        if frase[i] == ',' or frase[i] == '-' or frase[i] == ':' or frase[i] == ';' or frase[i] == '!' or frase[i] == '?':
            frase = frase[:i] + ' ' + frase[i+1:]
       	elif frase[i] == '.' and frase[i] != '.':
            frase = frase[:i] + ' ' + frase[i+1:]
	return frase