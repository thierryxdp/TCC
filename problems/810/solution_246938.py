def retira_pontuacao(frase):
    a=str.replace(frase,"-"," ")
    b=str.replace(a,","," ")
    c=str.replace(b,":"," ")
    d=str.replace(c,";"," ")
    e=str.replace(d,"."," ")
    f=str.replace(e,"?"," ")
    g=str.replace(f,"!"," ")

    return g


def inverte(frase):
    a=retira_pontuacao(frase)
    b=str.split(a)
    c=b[::-1]
    d=str.join(' ',c)
    e=str.lower(d)

    return e