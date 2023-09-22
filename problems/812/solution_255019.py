def retira_pontuacao(frase):
    '''funcao que retira toda a pontuacao de uma frase
     str->str'''
    for a in [',','.',';',':','!','?','-']:
        if a in frase:
            texto=frase.replace(a,' ')
            return texto.replace(a,' ')