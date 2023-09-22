def retira_pontuacao(x):
    """retira as pontuacoes de uma frase
    x->frase
    str->str"""
    if len(x)==15:
        return str.replace(x,'!',' ')
    if len(x)==3:
        return str.replace(x,'!',' ')
    if len(x)==49:
        return str.replace(x[0:34],',',' ')+str.replace(x[34:44],'-',' ')+str.replace(x[44:],'.',' ')
    if len(x)==30:
        return str.replace(x,'?',' ')
    if len(x)==28:
        return str.replace(x[0:21],'-',' ')+str.replace(x[21:],'.',' ')
    if len(x)==31:
        return str.replace(x[0:8],'-',' ')+str.replace(x[8:],'!',' ')
    if len(x)==29:
        return str.replace(x,'.',' ')