def retira_pontuacao(frase):
    """coment"""
    s0=frase
    s1=str.replace(s0,"-"," ")
    s2=str.replace(s1,","," ")
    s3=str.replace(s2,":"," ")
    s4=str.replace(s3,";"," ")
    s5=str.replace(s4,"."," ")
    return s5