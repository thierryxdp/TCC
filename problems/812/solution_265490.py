def retira_pontuacao(frase):
    return str.strip(frase, ".") + str.strip(frase, ",") + str.strip(frase, ":")