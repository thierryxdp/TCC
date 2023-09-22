def retira_pontuacao (frase):
    """Função que, dada uma frase como valor de entrada, retorna a
    mesma frase porém substituindo todos os sinais de pontuação (travessão,
    vírgula, ponto e vírgula, dois pontos, reticências, ponto final,
    interrogação e exclamação) por espaços.
    str -> str"""
    reticencias = str.replace(frase,"..."," ")
    interrogacao = str.replace(reticencias,"?", " ")
    exclamacao = str.replace(interrogacao,"!", " ")
    ponto_final = str.replace(exclamacao, ".", " ")
    virgula = str.replace(ponto_final, ",", " ")
    ponto_virgula = str.replace(virgula, ";", " ")
    dois_pontos = str.replace(ponto_virgula, ":" , " ")
    travessao = str.replace(dois_pontos,"-", " ")
    return travessao