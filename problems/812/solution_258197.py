def retira_pontuacao (frase):
    """função que recebe uma frase normal e que retorna uma nova frase sem
    todos os pontos: vírgula, travessão, dois pontos, ponto e vírgula e
    ponto final) e substituir todos eles por um espação;
    string->string"""
    virgula = str.replace(frase,',',' ')
    travessao = str.replace(virgula,'-',' ')
    dois_pontos = str.replace(travessao,':',' ')
    ponto_virgula = str.replace(dois_pontos,';',' ')
    ponto_final = str.replace(ponto_virgula,'.',' ')
    ponto_exclamacao = str.replace(ponto_final,'!',' ')
    ponto_interrogacao = str.replace(ponto_exclamacao,'?',' ')
    
    return ponto_interrogacao