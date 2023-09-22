def retira_pontuacao(frase)
	a=str.replace(frase,"—"," ")
    b=str.replace(a,","," ")
    c=str.replace(b,":"," ")
    d=str.replace(c,";"," ")
    e=str.replace(d,"."," ")
    f=str.replace(e,"!"," ")
    g=str.replace(f,"?"," ")
    h=str.replace(g,"..."," ")
    i=str.replace(h,"-"," ")
    return i

def inverte(frase):
    return str.join(" ",str.split(str.lower(retira_pontuacao(frase)))[-1::-1]