def retira_pontuacao(frase):
    """Função que recebe uma frase como parâmetro de entrada e
    retorna a mesma frase,sendo que, todos os caracteres de pontua-
    ção (incluindo travessão, vírgula, dois pontos, ponto e vírgula e pon-
    tuação de encerramento de frase) serão substituídos por espaço.
    Entrada: str
    Saída: str
    """
    
    t=str(frase)
    
    t = str.replace(t, '-', ' ')
    t = str.replace(t, ',', ' ')
    t = str.replace(t, ':', ' ')
    t = str.replace(t, ';', ' ')
    t = str.replace(t, '.', ' ')
    t = str.replace(t, '-', ' ')
    t = str.replace(t, '?', ' ')
    t = str.replace(t, '!', ' ')
    
    
    return t