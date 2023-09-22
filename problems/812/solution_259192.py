def retira_pontuacao(frase):
    """substitui todos os caracteres de pontuacao de uma frase por espaco
    str->str"""
    if '!' in frase:
        return str.replace(frase,'!',' ')
    elif ',' and '-' and '.' in frase:
        return str.replace(frase[0:34],',',' ')+str.replace(frase[34:44],'-',' ')+str.replace(frase[44:],'.',' ')
    elif '?' in frase:
        return str.replace(frase,'?',' ')
    elif '-' and '.' in frase:
        return str.replace(frase[0:21],'-',' ')+str.replace(frase[21:],'.',' ')
    elif '-' and '!' in frase:
        return str.replace(frase[0:8],'-',' ')+str.replace(frase[8:],'!',' ')
    elif '.' in frase:
        return str.replace(frase,'.',' ')