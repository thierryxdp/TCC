def retira_pontuacao(frase):
    '''funcao que retira toda a pontuacao de uma frase
     str->str'''
    for (',' or '.' or ';' or ':' or '-' or '!' or '?') in frase:
        return frase.replace(',' or '.' or ';' or ':' or '-' or '!' or '?',' ')