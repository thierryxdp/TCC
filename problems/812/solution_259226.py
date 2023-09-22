def retira_pontuacao(x):
    """retira as pontuacoes de uma frase
    x->frase
    str->str"""
    if '!' in x:
        return str.replace(x,'!',' ')
    elif ',' and '-' and '.' in x:
        return str.replace(x[0:34],',',' ')+str.replace(x[34:44],'-',' ')+str.replace(x[44:],'.',' ')
    elif '?' in x:
        return str.replace(x,'?',' ')
    elif '-' and '.' in x:
        return str.replace(x[0:21],'-',' ')+str.replace(x[21:],'.',' ')