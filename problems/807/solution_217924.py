def conta_frases(frase):
    '''
    Recebe a frase(str) e calcula quantas pontuações existem nela.
    Para achar (".") sozinhos é simples diminuir 3 vezes a quantidade de ("...")
    de todos (".").
    retorna quantidade de pontos(int)
    '''
    pontos = frase.count("!")
    pontos += frase.count("?")
    pontos += frase.count("...")
    pontos += frase.count(".")-3*frase.count("...")
    return pontos