def retira_pontuacao(frase):
    """retorna a frase fornecida com todos os elementos de pontuação substituidos por espaços"""
    """str -> str"""
    a = str.replace(frase, '...',' ')
    b = str.replace(a, '-',' ')
    c = str.replace(b, '.',' ')
    d = str.replace(c, ';',' ')
    e = str.replace(d, '?',' ')
    f = str.replace(e, ':',' ')
    g = str.replace(f, ',',' ')
    h = str.replace(g, '!',' ')
    frase = h
    
    return frase

def inverte(Frase):
    
    Frase = retira_pontuacao(Frase)
    Frase = str.lower(Frase)
    l = str.split(Frase)
    list.reverse(l)
    return str.join(" ",l)

inverte("Anda apanhar um capotinho, Capitu, dizia-lhe ele.")