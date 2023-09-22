def retira_pontuacao(frase):
    """Funçao que, dada uma frase, retorna-a com todos os seus caracteres de pontuaçao (travessao, vírgula, dois pontos, ponto e vírgula e pontuaçao de encerramento) trocados por espaço
       str->str"""
    
    frase2=frase[:]
    for caractere in["-", ",", ":", ".", ";", "!", "?"]:
        frase2=str.replace(frase, caractere, " ")
        return frase2