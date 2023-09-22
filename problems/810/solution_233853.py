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

def inverte(frase):
    '''Dada uma frase retorna outra frase que contém as mesmas palavras da
    frase de entrada na ordem inversa, sem letras maiúsculas e sem a pontuação
    str -> str'''

    frase = retira_pontuacao(frase)
    frase = str.lower(frase)

    palavrasFrase = str.split(frase, " ")
    invertePalavras = palavrasFrase[-1::-1]

    fraseInversa = str.join(" ", invertePalavras)

    return fraseInversa[:-1]