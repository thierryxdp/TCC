def retira_pontuacao(texto):
    "Troca todos os caracteres de pontuação por espaços; str -> str"
    import re
    lista = re.split("[.!?:;/,]", texto)
    for frase in lista:
        if frase == "":
            lista.remove(frase)
    for frase in lista:
        if frase == "":
            lista.remove(frase)
    x = 0
    for espaco in lista(0,len(lista)):
        frase = ""
    	frase = frase+lista[x]+" "
    return frase