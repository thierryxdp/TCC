def retira_pontuacao(frase):
    f1 = str.replace(frase, ".", " ")
    f2 = str.replace(f1, "!", " ")
    f3 = str.replace(f2, "?", " ")
    f4 = str.replace(f3, "-", " ")
    f5 = str.replace(f4, ",", " ")
    f6 = str.replace(f5, ":", " ")
    f7 = str.replace(f6, ";", " ")
    return f7

def inverte(frase):
    lista = frase.split()
    nova_lista = lista[::-1]
    return retira_pontuacao(str.lower(str.join(" ",nova_lista)))