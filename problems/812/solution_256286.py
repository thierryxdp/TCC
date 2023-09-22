def retira_pontuacao(frase):
    return texto.count("!")+texto.count("?")+(texto.count(".")-(2*texto.count("...")))+texto.count("-")+texto.count(",")+texto.count(":")+texto.count(";")