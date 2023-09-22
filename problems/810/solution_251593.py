def inverte(frase):
    '''Retorna a frase dada como parâmetro invertida e sem pontuação
    	str -> str'''
    frase = str.split(retira_pontuacao(str.lower(frase)))
    return str.join(' ', frase[::-1])