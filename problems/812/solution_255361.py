def retira_pontuacao(frase):
    """Retorna uma (frase) sem sua pontuação(,.?!:-)
    str-->str""""
    tira_ponto = str.replace(frase,"."," ")
    tira_virgula = str.replace(tira_ponto,","," ")
    tira_interrogacao = str.replace(tira_virgula,"?"," ")
    tira_travessao = str.replace(tira_interrogacao,"-"," ")
    tira_doispontos = str.replace(tira_travessao,":"," ")
    tira_exclamacao = str.replace(tira_doispontos,"!"," ")
    tira_interrogacao = str.replace(tira_exclamacao,"?"," ")
    return tira_interrogacao