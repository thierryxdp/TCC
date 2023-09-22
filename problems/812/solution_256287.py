def retira_pontuacao(texto):
    return texto.count("!")+texto.count("?")+(texto.count(".")-(2*texto.count("...")))+texto.count("-")+texto.count(",")+texto.count(":")+texto.count(";")