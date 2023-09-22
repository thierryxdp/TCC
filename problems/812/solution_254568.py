def retira_pontuaçao(frase):
    """Função que, dada uma frase, retorne a frase onde todos os caracteres
    de pontuação, incluindo travessão, vírgula, dois pontos, ponto e vírgula,
    além da pontuação de encerramento de frase, tenham sido substituídos
    por espaço.
    str -> str
    """
    
    return str.replace(str.replace(str.replace(str.replace(frase.replace(',',' '),'.',' '),':',' '),'-',' '),';',' ')