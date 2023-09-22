def retira_pontuacao(frase):
    '''Recebe uma frase e troca todos os caracteres de pontuação (travessão,
    vírgula, dois pontos, ponto e vírgula, e pontuação de encerramento da frase)
    str -> str '''

    fraseEsp = str.replace(frase, "-", " ")
    fraseEsp = str.replace(fraseEsp, ",", " ")
    fraseEsp = str.replace(fraseEsp, ":", " ")
    fraseEsp = str.replace(fraseEsp, ";", " ")
    fraseEsp = str.replace(fraseEsp, "...", " ")
    fraseEsp = str.replace(fraseEsp, "!", " ")
    fraseEsp = str.replace(fraseEsp, "?", " ")
    fraseEsp = str.replace(fraseEsp, ".", " ")

    return fraseEsp