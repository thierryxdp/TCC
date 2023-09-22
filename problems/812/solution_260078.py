def retira_pontuacao(frase: str) -> str:
    '''Recebe uma frase e a retorna com espaço no lugar da pontuacao'''
    frase = frase.replace('.', ' ')
    frase = frase.replace('-', ' ')
    frase = frase.replace(',', ' ')
    frase = frase.replace(':', ' ')
    frase = frase.replace(';', ' ')
    frase = frase.replace('!', ' ')
    frase = frase.replace('?', ' ')
    return frase