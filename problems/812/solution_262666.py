def retira_pontuacao(frase):
    """essa função , dada uma frase(igual ao parâmetro de entrada frase), retorna a
frase onde todos os caracteres de pontuação (incluindo travessão, vírgula, dois pontos,
ponto e vírgula, além da pontuação de encerramento de frase) foram substituídos por 
espaço.
string->string"""
    return str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase,'.',' '), '?',' '),'!',' '),'-',' '),',',' '),';',' '),':',' ')