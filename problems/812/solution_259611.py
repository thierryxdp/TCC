def retira_pontuacao(frase):
    #para cada símbolo, cria lista e refaz texto com join
    lista = frase.split("-")
    frase = " ".join(lista)
    lista = frase.split(",")
    frase = " ".join(lista)
    lista = frase.split(":")
    frase = " ".join(lista)
    lista = frase.split("!")
    frase = " ".join(lista)
    lista = frase.split("?")
    frase = " ".join(lista)
    lista = frase.split(";")
    frase = " ".join(lista)
    lista = frase.split(".")
    frase = " ".join(lista)
    return frase