def retira_pontuacao(frase:str)->str:
    return frase.replace('-', ' ').replace(',', ' ').replace(':', ' ').replace(';', ' ').replace('.', ' ').replace('!', ' ').replace('?', ' ').replace('...', ' ')

def inverte(frase:str)->str:
    frase = retira_pontuacao(frase).lower()
    return ' '.join(frase.split(' ').reverse())