def retira_pontuacao(f: str) -> str:
    """ dado uma frase, retorna a frase onde todos os caracteres de
    pontuação(incluindo travessão, vírgula, dois pontos, ponto e vírgula,
    além da pontuação de encerramento de frase) são substituídos por espaço.
    """
    
    f = []
    """ fsp = Frase Sem Pontuação"""
    
    fsp = str.replace(f, ":", " ")
    fsp = str.replace(f, ",", " ")
    fsp = str.replace(f, ".", " ")
    fsp = str.replace(f, ";", " ")