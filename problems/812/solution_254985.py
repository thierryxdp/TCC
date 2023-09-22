def retira_pontuacao(frase):
    '''funcao que retira toda a pontuacao de uma frase
     str->str'''
    import string
    p=string.punctuation
    s=frase
    if '?' in p:
        return s.replace('?', ' ')
    elif '!' in p:
        return s.replace('!', ' ')