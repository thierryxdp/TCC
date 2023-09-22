def inverte(frase):
    a=retira_pontuacao(frase)
    b=str.split(a)
    c=b[::-1]
    d=str.join(' ',c)
    e=str.lower(d)

    return e