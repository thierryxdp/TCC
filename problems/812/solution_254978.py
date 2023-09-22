def retira_pontuacao(frase):
    '''funcao que retira toda a pontuacao de uma frase
     str->str'''
    import string
    p=sting.punctuation
    s=frase
    for ',' or '.' or ';' or ':' or '-' or '!' or '?' in p:
        return s.replace(',' or '.' or ';' or ':' or '-' or '!' or '?', ' ')