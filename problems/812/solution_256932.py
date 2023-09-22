def retira_pontuacao(frase):
    """ Função que dada uma frase, retorna a frase onde todos os caracteres de pontuação
    (incluindo travessão, vírgula, dois pontos, ponto e vírgula, além da pontuação de encerramento de frase)
    tenham sido substituidos por espaço """
    frase_virgula=str.replace(frase, ","," ")
    frase_virgula_sem_ponto=str.replace(frase_virgula, "."," ")
    frase_sem_travessao=str.replace(frase_virgula_sem_ponto, "-"," ")
    frase_sem_ponto_virgula=str.replace(frase_sem_travessao, ";"," ")
    frase_sem_dois_pontos=str.replace(frase_sem_ponto_virgula, ":"," ")
    frase_sem_exclamacao=str.replace(frase_sem_dois_pontos, "!"," ")
    frase_sem_interrogacao=str.replace(frase_sem_exclamacao, "?"," ")
    return frase_sem_interrogacao