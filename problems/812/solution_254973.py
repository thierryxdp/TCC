def retira_pontuacao(frase):
    '''funcao que retira toda a pontuacao de uma frase
     str->str'''
    x=',' or '.' or ';' or ':' or '-' or '!' or '?'
    for x in frase:
        return frase.replace(x,' ')