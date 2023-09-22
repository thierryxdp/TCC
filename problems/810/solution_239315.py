def retira_pontuacao(frase):
    """Função que substitui pontuação por espaços."""
    """ Str -> Str"""
    frase = frase.replace(":"," ").replace("-"," ").replace(","," ").replace(";"," ").replace("."," ").replace("!"," ").replace("?"," ")
	return frase

def inverte(frase):
    """Função que retorna uma frase de trás para frente."""
    """ Str -> Str"""
    frase = frase.lower(retira_pontuacao(frase))
    return frase.split().reverse().join(" ",frase)