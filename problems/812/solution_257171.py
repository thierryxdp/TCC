def retira_pontuacao (frase):
    """essa função irá retornar a frase sem pontuação e irá incluir espaço onde foram retiradas as pontuações; str -> str"""
    RP = frase.replace ("-", " ").replace(",", " ").replace(":", " ").replace(";", " ").replace(".", " ").replace("!", " ").replace("?", " ")
    return RP