def retira_pontuacao(frase):
    """Retornar uma função que, dada uma frase, retira-se a pontuação da mesma e que sejam substituídas por espaços; str=>str"""
	exclamacao = str.replace(frase,"!", " ")
    interrogacao = str.replace(exclamacao,"?", " ")
    virgula = str.replace(interrogacao,",", " ")
    reticencias = str.replace(virgula, "...", " ")
    ponto = str.replace(reticencias,".", " ")
    dois_pontos = str.replace(ponto,":", " ")
    ponto_vitgula = str.replace(dois_pontos,";", " ")
    travessao = str.replace(ponto_virgula,"-", " ")
    return travessao