def retira_pontuacao(texto):
    dois_pontos = str.replace (texto, ":", "")
    travessao = str.replace (dois_pontos, "-", " ")
    pvirg = str.replace (travessao, ";", "")
    retic = str.replace (pvirg, "...", "")
    exc = str.replace (retic, "!", "")
    inter = str.replace (exc, "?", "")
    virgula = str.replace (inter, ",", "")    
    ponto = str.replace (virgula, ".", "")
    return ponto

def inverte(texto):
    """Inverte a ordem das palavras imputadas como frase, excluindo letras maiúscula e pontuação.
    assinatura: str --> str
    testes:
    inverte'O dia está lindo')==lindo está dia o
    inverte('Devemos trabalhar muito')==muito trabalhar devemos
    """
	notpont = retira_pontuacao(texto)
    textolower = str.lower(notpont)
    textopart = str.split(textolower, " ")
    list.reverse(textopart)
    final = str.join(" ", textopart)
    return final