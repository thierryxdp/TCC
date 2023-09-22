def retira_pontuacao(s):
    """
    Dada uma string substitui sua pontuacao por espaço
    Parametro:
    	s -> str
        Frase a ser modificada
    Returns:
    	str
        a frase sem pontos
    """
    return str.replace(str.replace(str.replace(str.replace(str.replace(s,"-"," "),","," "),":"," "),";"," "),"."," ")