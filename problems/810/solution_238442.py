def pontuacao(frase3):
    a = str.replace(frase3,'.','')
    b = str.replace(a,",",'')
    c = str.replace(b,';','')
    d = str.replace(c,':','')
    e = str.replace(d,"-",' ')
    f = str.replace(e,'!','')
    g = str.replace(f,'?','')
    return g

def inverte(frase4):
    '''Função que retorne uma frase ao contrário mas sem letras maiúsculas e sem
        pontuação. Entrada: list(str) ; Saída: list(str)'''
    p1= pontuacao(frase4)
    p2 = str.lower(p1)
    p3 = str.split(p2, " ")
    p4 = p3[::-1]
    p5 = str.join(" ",p4)
    return p5