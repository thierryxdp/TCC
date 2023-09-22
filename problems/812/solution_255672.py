def retira_pontuacao(frase):
    '''retira toda a pontuação da frase recebida'''
	a=str.replace(frase,"!"," ")
    b=str.replace(a,"?"," ")
    c=str.replace(b,"..."," ")
    d=str.replace(c, "," ,' ')
    e=str.replace(d, "." ," ")
    f=str.replace(e,":"," ")
    g=str.replace(f,";"," ")
    h=str.replace(g,"-"," ")
    frasef=str.replace(h,"_"," ")
    return frasef