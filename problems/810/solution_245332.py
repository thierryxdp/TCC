def retira_pontuacao(frase):
    trave=frase.replace('-',' ')
    virgula=frase.replace(',',' ')
    virgula_trave=trave.replace(',',' ')
    
    if ('-' and '.' and ',') in frase:
        return str.replace (virgula_trave,'.',' ')
    elif ('-' and '.') in frase and not ','  in frase:
        return trave.replace('.',' ')
    elif ('-' and '!') in frase:
        return trave.replace('!',' ')
    elif ('.') in frase:
        return frase.replace('.',' ')
    elif '?' in frase:
        return frase.replace('?',' ') 
    elif ('!' and not '-')in frase:
        return frase.replace('!',' ')
    elif ',' in frase:
        return str.replace(virgula,'.',' ')
    elif ';' in frase:
        return frase.replace(';',' ')
    elif ':' in frase:
        return frase.replace(':',' ')
def inverte(frase):
    retira_pontuacao
    sem_pont=retira_pontuacao(frase)
    invertida = sem_pont[::-1]
    invertida.split(' ')
    
    return invertida[::-1]