def retira_pontuacao(frase):
    """funcao que retorna a frase de entrada onde todos os caracteres de pontuacao tenham sido substituidos por espaco
    str -> str"""
    string=frase
    if ',' in frase:
        str.replace(frase,',',' ')=string
    if '?' in frase:
        str.replace(frase,'?',' ')=string
    if '!' in frase:
        str.replace(frase,'!',' ')=string
    if '.' in frase:
        str.replace(frase,'.',' ')=string
    if ':' in frase:
        str.replace(frase,':',' ')=string
    if '-' in frase:
        str.replace(frase,'-',' ')=string
    if ';' in frase:
        str.replace(frase,';',' ')=string
    return string