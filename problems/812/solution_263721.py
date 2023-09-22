def retira_pontuacao(frase):
    pontoFinal = frase.replace("..."," ")
    interrogacao = pontoFinal.replace("?"," ")
    exclamacao = interrogacao.replace("!"," ")
    travessao = exclamacao.replace("-"," ")
    virgula = travessao.replace(","," ")
    doisP = virgula.replace(":"," ")
    reticencias = doisP.replace("."," ")
    return reticencias