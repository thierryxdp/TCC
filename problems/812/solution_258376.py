def retira_pontuacao(frase) :
    """Retira todos os caracteres de pontuação dada uma frase;
    str -> str"""
    s = [".",",",":",";","!","?","-"]
    d = str(str.sprit(frase))
    return str.replace(d,s," ")