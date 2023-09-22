def inverte(frase):
    a= retira_pontuacao(frase)
    b= str.split(a," ")
    c= list.reverse(b)
    d= str.join(" ",b)
    e= str.lower(d)
    return e