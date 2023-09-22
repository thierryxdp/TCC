def retira_pontuacao(frase):
    """
    Retorna uma frase onde todos os caracteres da pontuação (ponto, 
    reticências, interrogação, exclamação, travessão, vírgula, 
    dois pontos e ponto e vírgula) são substituídos por espaço;
    str -> str
    """
    F0 = frase.replace("."," ")
    F1 = frase.replace("..."," ")
    F2 = frase.replace("?"," ")
    F3 = frase.replace("!"," ")
    F4 = frase.replace("-"," ")
    F5 = frase.replace(","," ")
    F6 = frase.replace(":"," ")
    F7 = frase.replace(";"," ")
    return F0+F5