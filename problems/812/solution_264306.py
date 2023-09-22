def retira_pontuacao(frase):
    if '.' in frase:
        return (frase.replace('.', ' '))
    elif '-' in frase:
        return (frase.replace('-', ' '))
    elif ',' in frase:
        return (frase.replace(',',' '))
    elif ':' in frase:
        return (frase.replace(':', ' '))
    elif ';' in frase:
        return (frase.replace(';', ' '))