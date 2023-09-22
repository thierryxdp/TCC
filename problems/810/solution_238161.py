def retira_pontuacao(frase):
    """Função que, dada uma frase, substitui todos os caracteres de pontuação
por espaços"""
    a = str.replace(frase,'?','')
    b = str.replace(a,'!','')
    c = str.replace(b,'...','')
    d = str.replace(c,'.','')
    e = str.replace(d,'-','')
    f = str.replace(e,',','')
    g = str.replace(f,':','')
    h = str.replace(f,';','')
    return h

def inverte(frase):
    """Função que, dada uma frase, remove suas pontuações, letras maiúsculas
e a retorna na ordem inversa"""
    i = str.lower(frase)
    j = retira_pontuacao(i)
    k = str.split(j,' ')
    l = k[::-1]
    m = str.join(' ',l)
    return m