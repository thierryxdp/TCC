def retira_pontuacao(frase):
    lista=frase.split()
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