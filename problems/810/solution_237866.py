def inverte(frase):
    """Essa função irá retornar uma determinada frase na sua ordem inversa ; str -> str"""
    frase = frase.lower()
    a = retira_pontuacao(frase)

    string = a.split()
    string.reverse()
    string = ' '.join(string)
    

    return string