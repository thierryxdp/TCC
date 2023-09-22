def retira_pontuacao(frase):
    tira_travesao = str.replace(frase, "-", " ")
    tira_virgula = str.replace(tira_travessao, ",", " ")
    tira_doispontos = str.replace(tira_virgula, ":", " ")
    tira_pontovirgula = str.replace(tira_doispontos, ";", " ")
    tira_ponto = str.replace(tira_pontovirgula, ".", " ")
    return tira_ponto