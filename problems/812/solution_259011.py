def retira_pontuacao(f: str):
    """ dado uma frase, retorna a frase onde todos os caracteres de
    pontuação(incluindo travessão, vírgula, dois pontos, ponto e vírgula,
    além da pontuação de encerramento de frase) são substituídos por espaço.
    """
    
    f == ()
    """ fsp = Frase Sem Pontuação"""
    
    fsp = str.replace(f, ":", " ")
    fsp1 = str.replace(fsp, ",", " ")
    fsp2 = str.replace(fsp1, ".", " ")
    fsp3 = str.replace(fsp2, ";", " ")
    fsp4 = str.replace(fsp3, "!", " ")
    fsp5 = str.replace(fsp4, "-", " ")
    fsp6 = str.replace(fsp5, "?", " ")
    return fsp6