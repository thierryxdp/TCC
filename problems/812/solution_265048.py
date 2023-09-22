def retira_pontuacao(texto):
    """
    Essa fução, dado como argumento um texto, ira retirar todo tipo de pontuação do mesmo
    e ira substituir por ' ' ( espaço)
    str->str
    """
    a = str.replace(texto,'-',' ')
    b = str.replace(a,',',' ')
    c = str.replace(b,':',' ')
    d = str.replace(c,';',' ')
    e = str.replace(d,'.',' ')
    f = str.replace(e,'?',' ')
    g = str.replace(f,'!',' ')
    return g