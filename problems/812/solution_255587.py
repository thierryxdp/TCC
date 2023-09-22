def retira_pontuacao(s):
    """dada uma frase,retorna a frase sendo que todos os caracteres de pontuação são substituídos por espaço;str->str"""
    s1=str.replace(s,"!"," ")
    s2=str.replace(s1,"?"," ")
    s3=str.replace(s2,"."," ")
    s4=str.replace(s3,","," ")
    s5=str.replace(s4,";"," ")
    s6=str.replace(s5,":"," ")
    s7=str.replace(s6,"-"," ")
    return s7