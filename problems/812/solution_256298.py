def retira_pontuacao(frase):
    """Função que dada uma frase, retorna a frase onde todos os caracteres de 
    pontuação (incluindo travessão, vírgula, dois pontos, ponto e vírgula, além
    da pontuação de encerramento de frase) tenham sido substituídos por espaço.
    Dados de entrada: str
    Dados de saida: str"""
    if str.count(frase, '-') != 0:
        return str.replace(str.replace(frase, ',', ' '), '.', ' ')
    if str.count(frase, '-') != 0:
        return str.replace(str.replace(frase, ',', ' '), '.', ' ')