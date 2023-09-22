def pontuacao(frase1):
    a = str.replace(frase1,'.','')
    b = str.replace(a,",",'')
    c = str.replace(b,';','')
    d = str.replace(c,':','')
    e = str.replace(d,"-",' ')
    f = str.replace(e,'!','')
    g = str.replace(f,'?','')
    return g

def inverte(frase2):
    '''Função que retorne uma frase ao contrário mas sem letras maiúsculas e sem
        pontuação. str -> str'''
    p1= pontuacao(frase2)
    p2 = str.lower(p1)
    p3 = str.split(p2, " ")
    p4 = p3[::-1]
    p5 = str.join(" ",p4)
    return p5