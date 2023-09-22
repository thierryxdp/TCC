def retira_pontuacao(frase):
    """Função que substitui pontuação por espaços."""
    """ Str -> Str"""
    frase = frase.replace(":"," ").replace("-"," ").replace(","," ").replace(";"," ").replace("."," ").replace("!"," ").replace("?"," ")
	return frase

def inverte(frase):
    """Função que retorna uma frase de trás para frente."""
    """ Str -> Str"""
    frase = retira_pontuacao(frase).lower().split()
    return " ".join(frase[::-1])