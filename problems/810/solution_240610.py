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

def inverte(frase):
    frasesempont = retira_pontuacao(frase)
    #separa palavras
    lista = frasesempont.split()
    #inverte palavras
    listainvertida = lista[::-1]
    #junta tudo
    saida = " ".join(listainvertida)
    #tira maiúsculas
    saida = saida.lower()
    return saida