def retira_pontuacao (frase):
    """essa função irá retornar a frase sem pontuação e irá incluir espaço onde foram retiradas as pontuações; str -> str"""
    RP = frase.replace ("-", " ").replace(",", " ").replace(":", " ").replace(";", " ").replace(".", " ").replace("!", " ").replace("?", " ")
    return RP

def inverte(frase):
    """Essa função irá retornar uma determinada frase na sua ordem inversa ; str -> str"""
    frase = frase.lower()
    a = retira_pontuacao(frase)
    string = a.split()
    string.reverse()
    string = ' '.join(string)
    

    return string