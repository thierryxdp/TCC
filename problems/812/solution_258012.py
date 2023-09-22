def retira_pontuacao(frase):
    """dada uma frase retorna a mesma com os caracteres especiais substituidos por espaco
    str->str"""
    
    frase.replace("-"," ")
    frase.replace(","," ")
    frase.replace(":"," ")
    frase.replace(";"," ")
    frase.replace("."," ")
    frase.replace("!"," ")
    frase.replace("?"," ")   
    
    return frase