def retira_pontuacao(frase):
    '''funcao que retira toda a pontuacao de uma frase
     str->str'''
    pont=',' and '.' and ';' and ':' and '!' or '?' or '-'
    result= frase.replace(pont, ' ')
    return result