def retira_pontuacao(string:str)->str:

    """ Função que transforma todos os caracteres de pontuação de frase em espaço

        Parameters:

        string: A frase a ser modificada

        Returns:

        Frase substituindo as pontuações de travessão, vírgula, dois pontos,
        ponto e viírgula e ponto final por espaço


    """

    travessao = str.join(" ", str.split(string,"-"))
    virgula = str.join(" ", str.split(travessao,","))
    dois_pontos = str.join(" ", str.split(virgula,":"))
    ponto_e_virgula = str.join(" ", str.split(dois_pontos,";"))
    ponto_final = str.join(" ", str.split(ponto_e_virgula,"."))

    final = ponto_final

    return final