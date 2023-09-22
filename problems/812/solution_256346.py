def retira_pontuacao(frase):
    """Função que dada uma frase, retorne a frase onde todos os caracteres 
    de pontuação (incluindo travessão, vírgula, dois pontos, ponto e 
    vírgula, além da pontuação de encerramento de frase) tenham sido 
    substituídos por espaço. 
    Dados de entrada: str
    Dados de saida: str"""
    a = str.replace(frase, '-', ' ')
    a = str.replace(a, '.', ' ')
    a = str.replace(a, '?', ' ')
    a = str.replace(a, ',', ' ')
    a = str.replace(a, ':', ' ')
    a = str.replace(a, ';', ' ')
    return a