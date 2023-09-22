def retira_pontuacao(texto):
   """Função que, dada uma frase, retorna a frase onde
   todos os caracteres de pontuação (incluindo travessão,
   vírgula, dois pontos, ponto e vírgula, além da pontuação
   de encerramento de frase) tenham sido substituídos por
   espaço"""
    import re
    return re.sub(r'[^\w\s]','',texto)