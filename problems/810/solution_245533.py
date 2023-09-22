def retira_pontuacao(texto):
    "Troca todos os caracteres de pontuação por espaços; str -> str"
    import re
    lista = re.split("[.!?:;/,-]", texto)
    for frase in lista:
        if frase == "":
            lista.remove(frase)
    for frase in lista:
        if frase == "":
            lista.remove(frase)
    x = 0
    frase = ""
    while x < len(lista):
        frase = frase+lista[x]+" "
        x = x+1
    return frase
def inverte(frase):
    """Recebe uma frase, retira toda sua pontuação, substitui as letras maiúsculas por minúsculas
    e inverte toda a frase, depois á retorna; str -> str"""
    frase = retira_pontuacao(frase).lower()
    lista = frase.split()
    lista.reverse()
    frase = " ".join(lista)
    return frase