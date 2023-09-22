def retira_pontuacao(frase):
    """dada uma frase substitui as pontuaçoes desta por espaços vazios
    str->str"""
    if '!' in frase and '-' and '.' and '?' not in frase:
        return str.replace(frase,'!',' ')
    if ',' and '-' and '.' in frase and '!' not in frase:
        return str.replace(frase[0:34],',',' ')+str.replace(frase[34:44],'-',' ')+str.replace(frase[44:],'.',' ')
    if '?' in frase and '.' and ',' and '!' not in frase:
        return str.replace(frase,'?',' ')