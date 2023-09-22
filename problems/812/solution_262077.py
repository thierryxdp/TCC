def retira_pontuacao(frase):
    """
    Retorna uma frase onde todos os caracteres da pontuação (ponto, 
    reticências, interrogação, exclamação, travessão, vírgula, 
    dois pontos e ponto e vírgula) são substituídos por espaço;
    str -> str
    """
    if caractere in ".!?-,:;...":
        return frase.replace(caractere," ")
    else:
        return "Inválido"