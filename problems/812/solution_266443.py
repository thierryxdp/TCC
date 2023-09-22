def retira_pontuacao(s):
    """ Substitiu cada pontucao de uma string dada por um espaco
    str-->str
    """
    
    a=str.replace(s,"-"," ")
    b=str.replace(a,","," ")
    c=str.replace(b,":"," ")
    d=str.replace(c,";"," ")
    e=str.replace(d,"."," ")
    f=str.replace(e,"?"," ")
    g=str.replace(f,"!"," ")
    return g