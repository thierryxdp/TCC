def retira_pontuacao(frase):
    """retorna o negocio"""
    
    frase.replace("-"," ")
    frase.replace(","," ")
    frase.replace(":"," ")
    frase.replace(";"," ")
    frase.replace("."," ")
    frase.replace("!"," ")
    frase.replace("?"," ")
    
    return frase()