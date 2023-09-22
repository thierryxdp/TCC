def retira_pontuacao(frase):
    '''retorna a frase onde todos os caracteres de pontuação foram substituidos por espaço.string->string'''
    a=str.replace(frase,"-"," ")
    b=str.replace(a,","," ")
    c=str.replace(b,":"," ")
    d=str.replace(c,";"," ")
    e=str.replace(d,"."," ")
    f=str.replace(e,"?"," ")
    g=str.replace(f,"!"," ")
    return g