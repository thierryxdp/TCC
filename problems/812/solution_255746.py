def retira_pontuacao (frase):
    """função que recebe uma frase e retorna um espaço no lugar onde havia caracteres de pontuação
    string -> string"""
    x = frase
    a = str.replace (x,'.',' ')
    b = str.replace (a,',',' ')
    c = str.replace (b,'-',' ')
    d = str.replace (c,';',' ')
    e = str.replace (d,':',' ')
    f = str.replace (e,'?',' ')
    g = str.replace (f,'!',' ')
    return g