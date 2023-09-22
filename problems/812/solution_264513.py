def retira_pontuacao(frase):
    '''docs'''
    
    a = frase
    
    espaco = a.replace('-' and ',' and ':' and ';' and '.', ' ')
    
    return espaco