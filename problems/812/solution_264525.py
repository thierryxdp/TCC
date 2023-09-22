def retira_pontuacao(frase):
    '''docs'''
    
    a = frase
    
    b = a.replace(',', ' ')
    c = b.replace('.', ' ')
    
    return c