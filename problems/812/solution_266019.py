def retira_pontuacao(frase):
    i=frase.replace("?"," ")
    e=frase.replace("!"," ")
    ret=frase.replace("..."," ")
    pv=frase.replace(";"," ")
    pf=frase.replace(":"," ")
    t=frase.replace("-"," ")
    return i+e+ret+pv+pf+t