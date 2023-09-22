def retira_pontuacao(frase):
    ponto = str.replace(frase,".","¬")
    ponto_virgula = str.replace(ponto,";","¬")
    ponto_dois = str.replace(ponto_virgula,":","¬")
    virgula = str.replace(ponto_dois,",","¬")
    travessao = str.replace(virgula,"-","¬")
    exclamacao = str.replace(travessao,"!","¬")
    interrogacao = str.replace(exclamacao,"?","¬")
    espaco = str.replace(interrogacao,'¬',' ')
    return espaco