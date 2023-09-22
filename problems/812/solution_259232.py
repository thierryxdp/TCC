def retira_pontuacao(x):
    """retira as pontuacoes de uma frase
    x->frase
    str->str"""
    if '!' in x and '.' and ',' and '?' and '-' not in x:
        return str.replace(x,'!',' ')
    elif ',' and '-' and '.' in x and '?' and '!' not in x:
        return str.replace(x[0:34],',',' ')+str.replace(x[34:44],'-',' ')+str.replace(x[44:],'.',' ')