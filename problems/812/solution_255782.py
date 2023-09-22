def retira_pontuacao(frase):
    """essa funcao, dada uma frase como parametro de entrada,
	 substitui a pontuacao por espaco str -> str"""
    
    retira_ponto = str.replace(frase, ".", " ")
    retira_exclamacao = str.replace(retira_ponto, "!"," ")
    retira_virgula = str.replace(retira_exclamacao, ","," ")
    retira_interroga = str.replace(retira_virgula, "?"," ")
    retira_reticen = str.replace(retira_interroga, "..."," ")
    retira_doispontos = str.replace(retira_reticen, ":"," ")
    retira_pontovirg = str.replace(retira_doispontos, ";"," ")
    retira_travessao = str.replace(retira_pontovirg, "-"," ")
    
    retira_final = retira_travessao
    return retira_final