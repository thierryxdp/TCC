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
    tamanho = len(lista)
    x = 0
    for espaco in lista(0,tamanho):
        frase = ""
    	frase = frase+lista[x]+" "
    return frase