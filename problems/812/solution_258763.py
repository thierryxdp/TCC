def retira_pontuacao(frase):
    "A função retira os caracteres impostos pelo exercício, retornando uma nova frase. str -> str;"""
    frases= frase.replace("!", " ").replace("?", " ").replace(".", " ").replace(","," ").replace(":"," ").replace(";"," ").replace("-", " ")
    return frases