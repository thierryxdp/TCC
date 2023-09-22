def retira_pontuacao(frase):
    """dada uma frase retorna a mesma com os caracteres especiais substituidos por espaco
    str->str"""
    
    a = frase.replace("-"," ")
    b = a.replace(","," ")
    c = b.replace(":"," ")
    d = c.replace(";"," ")
    e = d.replace("."," ")
    f = e.replace("!"," ")
    g = f.replace("?"," ")   
    
    return g

def inverte(frase):
    """coisa"""
    
    fraseA = retira_pontuacao(frase)
    lista = fraseA.split()
    
    frase_final = str.join(" ",lista[-1::-1])
    
    return frase_final.lower()