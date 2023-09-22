def retira_pontuacao(frase):
    '''funcao que retira toda a pontuacao de uma frase
     str->str'''
    for a in [',','.',';',':','!','?','-']:
        if a in frase:
            frase1=frase.replace(a,' ')
            return frase1.replace(a,' ')