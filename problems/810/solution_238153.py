def retira_pontuacao(frase):
    """Função que, dada uma frase, substitui todos os caracteres de pontuação
por espaços"""
    a = str.replace(frase,'?',' ')
    b = str.replace(a,'!',' ')
    c = str.replace(b,'...',' ')
    d = str.replace(c,'.',' ')
    e = str.replace(d,'-',' ')
    f = str.replace(e,',',' ')
    g = str.replace(f,':',' ')
    h = str.replace(f,';',' ')
    return h

def inverte(frase):
    """Função que, dada uma frase, remove suas pontuações, letras maiúsculas
e a retorna na ordem inversa"""
    i = retira_pontuação(frase)
    j = str.lower(i)
    k = str.split(i,' ')
    l = len(k)
    m = k[-(l):-1]
    return m