def retira_pontuacao(frase):
    '''funcao que retira toda a pontuacao de uma frase
     str->str'''
    for a in [',','.',';',':','!','?','-']:
        if a in frase:
            texto=frase.replace(a,' ')
             p=texto.replace(a,' ')
                return p.replace(a,' ')