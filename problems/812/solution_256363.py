def retira_pontuacao(frase):
    """ """
    novaFrase = str.replace(frase,"/"," ") and str.replace(frase,","," ") and str.replace(frase,":"," ") and str.replace(frase,";"," ") and str.replace(frase,"."," ") and str.replace(frase,"!"," ") and str.replace(frase,"?"," ") and str.replace(frase,"-"," ")
    return novaFrase