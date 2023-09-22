def retira_pontuacao(frase):
    """Retornar uma função que, dada uma frase, retira-se a pontuação da mesma e que sejam substituídas por espaços; str=>str"""
	exclamacao = str.replace(frase,"!", " ")
    interrogacao = str.replace(frase,"?", " ")
    virgula = str.replace(frase,",", " ")
    reticencias = str.replace(frase, "...", " ")
    ponto = str.replace(frase,".", " ")
    dois_pontos = str.replace(frase,":" " ")
    ponto_vitgula = str.replace(frase,";", " ")
    travessao = str.replace(frase,"-", " ")
    return frase