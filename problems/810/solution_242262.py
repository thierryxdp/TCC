def inverte(frase):
    """retorna a frase invertida 
    str->str"""
    
    fraseA = retira_pontuacao(frase)
    lista = fraseA.split()
    
    frase_final = str.join(" ",lista[-1::-1])
    
    return frase_final.lower()