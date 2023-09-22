def retira_pontuacao(frase):
    """
    Essa função retorna o a frese sem sua pontuação, retirando
    travesão, vírgula, dois pontos, ponto e vírgula e ponto final.
    Parametro de Entrada: string
    Valor de Saída: list
    """
    f1=frase.("-"," ")
    f2=f1.replace(","," ")
    f3=f2.replace(":"," ")
    f4=f3.replace(";"," ")
    f5=f4.replace("."," ")
    f6=f5.replace("?"," ")
    f7=f6.replace("!"," ")
    return f7