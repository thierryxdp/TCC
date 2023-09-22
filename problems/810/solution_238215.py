def inverte(frase):
    '''Função que retorne uma frase ao contrário mas sem letras maiúsculas e sem
        pontuação. str -> str'''
    p1= pontuacao(frase)
    p2 = str.lower(p1)
    p3 = str.split(p2, " ")
    p4 = p3[::-1]
    p5 = str.join(" ",p4)
    return p5