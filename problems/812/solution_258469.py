def retira_pontuacao(frase):
    """ """
    if '.' in frase:
        return str.replace(frase,'.',' ')
    elif:
        return str.replace(frase,'!',' ')
    elif ',' in frase:
        return str.replace(frase,',',' ')
    elif '?' in frase:
        return str.replace(frase,'?',' ')
    else:
        return frase