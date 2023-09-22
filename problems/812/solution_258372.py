def retira_pontuacao(frase) :
    """Retira todos os caracteres de pontuação dada uma frase;
    str -> str"""
    s = str(".",",",":",";","!","?","-")
    return str.replace(frase,s," ")