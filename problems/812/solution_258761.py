def retira_pontuacao(frase):
    frases= frase.replace("!", " ").replace("?", " ").replace(".", " ").replace(","," ").replace(":"," ").replace(";"," ")
    return frases