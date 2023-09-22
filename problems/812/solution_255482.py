def retira_pontuacao(frase):
    """ Essa função, dada uma frase, retorna a mesma frase, só que com todos os caracteres de pontuação (incluindo travessão, vírgula, dois pontos, ponto e vírgula, além da pontuação de encerramento de frase) tenham sido substituídos por espaço.

        Parameters:
        frase = frase a ser inserida e avaliada

        Testes:
            retira_pontuacao() = "" 
            retira_pontuacao() = ""
            retira_pontuacao() = ""

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