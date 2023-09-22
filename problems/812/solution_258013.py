def retira_pontuacao(frase):
    """dada uma frase retorna a mesma com os caracteres especiais substituidos por espaco
    str->str"""
    
    a = frase.replace("-"," ")
    b = a.replace(","," ")
    c = b.replace(":"," ")
    d = c.frase.replace(";"," ")
    e = d.frase.replace("."," ")
    f = e.frase.replace("!"," ")
    g = f.frase.replace("?"," ")   
    
    return g