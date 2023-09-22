def retira_pontuacao(frase):
    '''funcao que retira toda a pontuacao de uma frase
     str->str'''
    import string
    p=string.punctuation
    s=frase
    if ',' in p and '.' and '?' in p:
        return s.replace(',' and '.' and '?', ' ')