def retira_pontuacao(frase):
    """Funcao que retira todas as pontuacoes de uma frase(string) e coloca no lugar um
    espaco vazio."""
    remocao = frase.replace("."," ")
    remocao = remocao.replace("!"," ")
    remocao = remocao.replace("?"," ")
    remocao = remocao.replace("..."," ")
    remocao = remocao.replace("-"," ")
    remocao = remocao.replace(","," ")
    remocao = remocao.replace(":"," ")
    remocao = remocao.replace(";"," ")
    return remocao