def retira_pontuacao(frase):
    'função que dado uma frase a retorna com espaço no lugar da pontuação'
    if '!' in frase:
        return frase.replace('!', ' ')
    elif '?' in frase:
        return frase.replace('?', ' ')
    elif '.' in frase:
        return frase.replace('.', ' ')
    elif ',' in frase:
        return frase.replace(',', ' ')
    elif '-' in frase:
        return frase.replace('-', ' ')