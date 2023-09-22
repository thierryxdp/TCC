def retira_pontuacao(frase):
    """Recebe uma frase como string e retorna a frase substituindo vírgula, travessão, dois pontos, ponto e vírgula e a pontuação de encerramento da frase por espaço. str ->."""
    r = frase
    if str.count(frase,',')>=1:
        frase = str.replace(frase,',')
    if str.count(frase,';')>=1:
        frase = str.replace(frase,';')
    if str.count(frase,'