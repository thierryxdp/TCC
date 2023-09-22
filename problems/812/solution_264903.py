def retira_pontuacao(frase):
    '''
    
    '''
    if '-' in (frase) or ',' in (frase) or ':' in (frase) or ';' in (frase) or '.' in (frase) or '!' in (frase) or '?' in (frase):
        return str.replace((frase), '-', ' ') + str.replace((frase), ',', ' ') + str.replace((frase), ':', ' ') + str.replace((frase), ';', ' ') + str.replace((frase), '.', ' ') + str.replace((frase), '!', ' ') + str.replace((frase), '?', ' ')