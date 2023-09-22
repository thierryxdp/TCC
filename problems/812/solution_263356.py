def retira_pontuacao(frase):
    '''Função que substitui todas as pontuações de uma frase por espaçamentos.
    frase -> string
    return -> string'''
    
    
    frase = frase.replace('-', ' ').replace(',', ' ').replace(':', ' ').replace(';',' ')
    frase = frase.rstrip(.).rstrip('?').rstrip('!')
    
    return frase + ' '