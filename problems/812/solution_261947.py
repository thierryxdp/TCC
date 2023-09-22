def retira_pontuacao(texto):
    "Troca todos os caracteres de pontuação por espaços; str -> str"
    import re
    lista = re.split("[.!?:-,]", texto)
    """for frase in lista:
        if frase == "":
            lista.remove(frase)
    for frase in lista:
        if frase == "":
            lista.remove(frase)"""
    for espaco in lista:
    	frase = frase+lista[espaco]+" "
    return frase