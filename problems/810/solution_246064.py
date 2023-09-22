def inverte(frase):
    tira_travessao = str.replace(frase, "-", "")
    tira_virgula = str.replace(tira_travessao, ",", "")
    tira_doispontos = str.replace(tira_virgula, ":", "")
    tira_pontovirgula = str.replace(tira_doispontos, ";", "")
    tira_ponto = str.replace(tira_pontovirgula, ".", "")
    tira_exclamacao = str.replace(tira_ponto, "!", "")
    tira_interrogacao = str.replace(tira_exclamacao, "?", "")
    frase = str.lower(tira_interrogacao)
    frase2 = frase[:]
    return frase