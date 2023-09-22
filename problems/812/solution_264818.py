def retira_pontuacao(frase):
    '''Função que dada uma frase, retorna a frase
    substituida por espaço no local onde tinha
    pontuações (travessão, vírgula, dois pontos,
    ponto e vírgula, além da pontuação de encerramento de frase
    str -> str'''
    travessao = str.count(frase,"-")
    if travessao!=0:
        return str.replace(frase,"-"," ",travessao)