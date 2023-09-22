def retira_pontuacao(frase):
    lista=list(frase.split())
    if ',' in frase:
        return frase.replace(',',' ')
    elif '!' in frase:
        return frase.replace('!',' ')
    elif '?' in frase:
        return frase.replace('?',' ')
    elif '-' in frase:
        return frase.replace('-',' ')
    elif '.' in frase:
        return frase.replace('.',' ')
    elif ',' and '-' in frase:
        return ' '.join(lista)