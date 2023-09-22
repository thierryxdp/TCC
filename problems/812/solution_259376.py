def retira_pontuacao(frase):
    """ Substitui todas as pontuação da frase fornecidadas 
        na função str->str"""
    frase = str.replace(frase,"!"," ")
    frase = str.replace(frase,"?"," ")
    frase = str.replace(frase,"."," ")
    frase = str.replace(frase,","," ")
    frase = str.replace(frase,"-"," ")
    frase = str.replace(frase,":"," ")
    frase = str.replace(frase,";"," ")
    return frase