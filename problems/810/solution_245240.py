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

def inverte(frase):
    """apos retirar a pontuaçao e transformar as letras maiusculas em minusculas, retorna o inverso da frase dada"""
    """str -> str"""
    
    frase = retira_pontuacao(frase)
    frase = str.lower(frase)
    l = str.split(frase)
    list.reverse(l)
    
    return str.join(" ",l)