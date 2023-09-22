def retira_pontuacao(texto):
    """Função que retorna a frase onde todos os caracteres de pontuação são substituídos por espaço"""
    """str-->str"""
    i = str.replace(texto, '...',' ')
    o = str.replace(i, '-',' ')
    u = str.replace(o, '.',' ')
    n = str.replace(u, ';',' ')
    m = str.replace(n, '?',' ')
    p = str.replace(m, ':',' ')
    q = str.replace(p, ',',' ')
    r = str.replace(q, '!',' ')
    texto=r
    return texto
def inverte(frase):
    """Função que apos retirar a pontuaçao e transformar as letras maiusculas em minusculas, retorna o inverso da frase dada"""
    """str -> str"""
    
    frase = retira_pontuacao(frase)
    frase = str.lower(frase)
    l = str.split(frase)
    list.reverse(l)
    
    return str.join(" ",l)