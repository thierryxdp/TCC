def retira_pontuacao(frase):
    """A função retirará todos os caracteres de pontuação
    e os substituirá por espaço
    Entrada: String
    Saida: String"""
    
    ('-',',',':',';') = pontuacao
    return str.replace(frase,pontuacao,' ')