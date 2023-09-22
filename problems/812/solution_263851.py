def retira_pontuacao(frase):
    '''função que retira toda a pontuação da frase sem exceções
    string -> string'''
    s1 = frase.replace('-', '')
    s2 = s1.replace('!', '')
    s3 = s2.replace('?', '')
    s4 = s3.replace(',', '')
    s5 = s4.replace(':', '')
    s6 = s5.replace(';', '')
    return s6