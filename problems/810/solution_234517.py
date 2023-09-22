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
    exclamacao = str.join(" ", str.split(ponto_final,"!"))
    interrogacao=str.join(" ", str.split(exclamacao,"?"))

    final = interrogacao

    return final

def inverte(frase:str)->str:

    """ Função que inverte sem letras maiúsculas e pontuações.

        Parameters:

        frase: A frase a ser modificada

        Returns:

        É retirado da frase todas as pontuações com a função retira_pontuacao
        e, depois, transforma-se todas as letras maiúsculas em minusculas. Por, fim é
        feito uma quebra da frase em uma lista de palavras para inverter a ordem e uni-las novamente


    """

    sem_pontuacao = retira_pontuacao(frase)
    letras_minusculas = str.lower(sem_pontuacao)
    separa_palavras = str.split(letras_minusculas)
    inverter_ordem = separa_palavras[::-1]
    juncao_palavras = str.join(" ",inverter_ordem)
    final = juncao_palavras

    return final