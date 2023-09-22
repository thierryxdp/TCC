def retira_pontuacao(frase):
    '''funcao que retira toda a pontuacao de uma frase
     str->str'''
    pont=',' or '.' or ';' or ':' or '!' or '?' or '-'
    result= frase.replace(pont, ' ')