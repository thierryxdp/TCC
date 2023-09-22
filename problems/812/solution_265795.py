def retira_pontuacao(f):
    '''Retira todos os caracteres de pontuação de uma frase f
    str -> str'''
    k='-,:;.!?'
    x in k:
    	list.replace(f,x,'')
    return f