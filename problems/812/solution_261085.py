def retira_pontuacao(frase):
    lista=frase.split()
    len(lista)=n
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
        return lista[0]+ ' '+lista[n]