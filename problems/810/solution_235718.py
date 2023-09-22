def retira_pontuacao(frase):
    '''retira toda a pontuação da frase recebida
    string->string'''
    a=str.replace(frase,"!"," ")
    b=str.replace(a,"?"," ")
    c=str.replace(b,"..."," ")
    d=str.replace(c, "," ,' ')
    e=str.replace(d, "." ," ")
    f=str.replace(e,":"," ")
    g=str.replace(f,";"," ")
    h=str.replace(g,"-"," ")
    frasef=str.replace(h,"_"," ")
    frasef=frasef.lower()
    return frasef
def inverte(frase):
    '''inverte uma frase dada sem sua pontuação e em letras minúsculas
    string->string'''
    return ' '.join(retira_pontuacao(frase).split()[::-1])