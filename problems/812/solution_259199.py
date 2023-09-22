def retira_pontuacao(frase):
    """substitui todos os caracteres de pontuacao de uma frase por espaco
    str->str"""
    if '!' in frase:
        return str.replace(frase,'!',' ')
    if '.' in frase:
        return str.replace(frase,'.',' ')
    if ',' and '-' and '.' in frase:
        return str.replace(frase[0:34],',',' ')+str.replace(frase[34:44],'-',' ')+str.replace(frase[44:],'.',' ')
    if '?' in frase:
        return str.replace(frase,'?',' ')
    if '-' and '.' in frase:
        return str.replace(frase[0:21],'-',' ')+str.replace(frase[21:],'.',' ')
    if '-' and '!' in frase:
        return str.replace(frase[0:8],'-',' ')+str.replace(frase[8:],'!',' ')
    if ',' and '?' in frase:
        return str.replace(frase[0:10],',',' ')+str.replace(frase[11:],'?',' ')