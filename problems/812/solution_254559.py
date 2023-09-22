def retira_pontuacao(frase):

    """ Retorna a frase dada onde todos os caracteres de pontuação 
        foram removidos;
        str->str
        Parametro:
        frase: frase dada
    """

    travessao = str.join(" ", str.split(frase,"-"))
    virgula = str.join(" ", str.split(travessao,","))
    dois_pontos = str.join(" ", str.split(virgula,":"))
    ponto_e_virgula = str.join(" ", str.split(dois_pontos,";"))
    ponto_final = str.join(" ", str.split(ponto_e_virgula,"."))
    exclamacao = str.join(" ", str.split(ponto_final,"!"))
    interrogacao=str.join(" ", str.split(exclamacao,"?"))

    final = interrogacao

    return final