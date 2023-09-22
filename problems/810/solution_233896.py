def retira_pontuacao(frase):
    """Dado como entrada uma frase contendo sinais de pontuação como
    "!","?","-",":",";",",", e "." , retorna esta frase sem estes caracteres
    de pontuação; str->str"""
    s0=frase
    s1=str.replace(s0,"-"," ")
    s2=str.replace(s1,","," ")
    s3=str.replace(s2,":"," ")
    s4=str.replace(s3,";"," ")
    s5=str.replace(s4,"."," ")
    s6=str.replace(s5,"!"," ")
    s7=str.replace(s6,"?"," ")
    return s7
def inverte(frase):
    """coment"""
    p0=str.lower(retira_pontuacao(frase))
    p1=str.split(p0," ")
    return str.join("",p1[::-1])