def retira_pontuacao(frase):
    sponto = str.replace(frase, ","," ")
    svirgula = str.replace(sponto, "."," ")
    stravessao = str.replace(svirgula, ":"," ")
    sdoisponto = str.replace(stravessao, "-"," ")
    spontovirgula = str.replace(sdoisponto, ";"," ")
    return spontovirgula