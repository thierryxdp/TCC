def retira_pontuacao(frase):
    '''funcao que retira toda a pontuacao de uma frase
     str->str'''
    for a in [',','.',';',':','!','?','-']:
        if a in frase:
            return frase.replace(a,' ')
        elif a in ['-','?']:
            return frase.replace(b,' ')