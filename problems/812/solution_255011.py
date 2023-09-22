def retira_pontuacao(frase):
    '''funcao que retira toda a pontuacao de uma frase
     str->str'''
    for a in [',','.',';',':','!','?','-']:
        if a in frase:
            return frase.replace(a,' ')
    for b in ['-','?']:
        elif b in frase:
            return frase.replace(b,' ')