def retira_pontuacao(frase:str)->str:
    return frase.replace('-', ' ').replace(',', ' ').replace(':', ' ').replace(';', ' ').replace('.', ' ').replace('!', ' ').replace('?', ' ').replace('...', ' ')