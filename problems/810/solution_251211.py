def retira_pontuacao(frase):
    """retorna uma frase onde todos os caracteres de pontuação tenham sido substituídos por espaço
    str->str"""
    caracteres = ["-", ",", ":", ";", ".","!","?"]
    for x in caracteres:
        frasenova = frase.replace(x," ")
        frase = frasenova
    return frase

def inverte(frasee):
    """retorna uma frase na ordem inversa sem letras maiúsculas e sem a pontuação
    str->str"""
    fraseea = retira_pontuacao(frasee)
    fraseea = fraseea.lower()
    fraseea = fraseea.split()
    fraseea = fraseea.reverse()
    fraseea = frassea.join(" ")
    return fraseea