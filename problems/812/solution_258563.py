def retira_pontuacao(frase):
    """"jhjhhi """"
    if '/' in frase:
        return str.replace(frase,'/',' ')
    if ',' in frase:
        return str.replace(frase,',',' ')
    if ':' in frase:
        return str.replace(frase,':',' ')
    if ';' in frase:
        return str.replace(frase,';',' ')
    if '.' in frase:
        return str.replace(frase,'.',' ')
    else:
        return str.replace(frase,'?',' ')