def retira_pontuacao(frase):
    """ funcao que retira todas as pontuaçoes de uma string 
    dada como estrada, substitui por espaço e retorna o 
    texto da string alterado.
    str->str"""
    a = str.replace(frase,"-"," ")
    b = str.replace(a,"?"," ")
    c = str.replace(b,"!"," ")
    d = str.replace(c,","," ")
    e = str.replace(d,":"," ")
    f = str.replace(e,";"," ")
    g = str.replace(f,"."," ")
    h = str.replace(g,"..."," ")
    return h