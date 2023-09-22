def retira_pontuacao(frase):
    """ Funçao que, dada uma frase,retorne a frase onde todos os caracteres de pontuação sejam substituidos por espaço"""
    list.remove(frase,'-')
    list.remove(frase,',')
    list.remove(frase,':')
    list.remove(frase,';')
    list.remove(frase,'.')
    list.remove(frase,'!')
    list.remove(frase,'?')
    list.remove(frase,'...')
    return frase