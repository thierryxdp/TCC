def inverte(Frase):
    """função que dada uma frase, retorne uma nova frase com as mesmas palavras que a anterior, de trás pra frente, sem pontuação e sem letras maiusculas; str-->str"""
    Frase= retira_pontuacao(Frase)
    str.lower(Frase)
    str.split(Frase)
    nova_Frase= Frase.join(Frase[::-1])
    return nova_Frase