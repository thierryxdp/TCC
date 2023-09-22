def retira_pontuacao(frase):
    ''' funcao que dada uma frase retorna outra frase onde toda a pontuacao foi subsituida por um espaco ('')'''
    if '-' in frase:
    frase.del(frase.index('-')) and frase.insert(frase.index('-'),'')
    return frase