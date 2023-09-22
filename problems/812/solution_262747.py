def retira_pontuacao(frase):
    """ Essa função, dada uma frase, retorna a mesma frase, só que com todos os caracteres de pontuação (incluindo travessão, vírgula, dois pontos, ponto e vírgula, além da pontuação de encerramento de frase) tenham sido substituídos por espaço.

        Parameters:
        frase = frase a ser inserida e avaliada

        Testes:
            retira_pontuacao("que fazia tudo!") = "que fazia tudo " 
            retira_pontuacao("Oh!") = "Oh "
            retira_pontuacao("Anda apanhar um capotinho, Capitu, dizia-lhe ele.") = "Anda apanhar um capotinho  Capitu  dizia lhe ele "

        Returns:
            a mesma frase, só que com todos os caracteres de pontuação (incluindo travessão, vírgula, dois pontos, ponto e vírgula, além da pontuação de encerramento de frase) tenham sido substituídos por espaço.
            str --> str
    """
    frase = str.replace(frase,"-"," ")
    frase = str.replace(frase,","," ")
    frase = str.replace(frase,":"," ")
    frase = str.replace(frase,";"," ")
    frase = str.replace(frase,":"," ")
    frase = str.replace(frase,"..."," ")
    frase = str.replace(frase,"."," ")
    frase = str.replace(frase,"!"," ")
    frase = str.replace(frase,"?"," ")
    return frase