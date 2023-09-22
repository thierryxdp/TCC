def retira_pontuacao(frase):
    """Função que substitui pontuação por espaços."""
    """ Str -> Str"""
    frase = frase.replace(":"," ").replace("-"," ").replace(","," ").replace(";"," ").replace("."," ").replace("!"," ").replace("?"," ")
    return frase