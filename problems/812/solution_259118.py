def retira_pontuacao(frase):
    remove_dois_pontos = frase.replace(":"," ")
    remove_ponto_virgula = remove_dois_pontos.replace(";"," ")
    remove_interrogacao = remove_ponto_virgula.replace("?"," ")
    remove_exclamacao = remove_interrogacao.replace("!"," ")
    remove_virgula = remove_exclamacao.replace(","," ")
    remove_ponto= remove_virgula.replace("."," ")
    return remove_ponto