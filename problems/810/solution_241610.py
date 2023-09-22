def retira_pontuacao(texto):
    texto1 = ' '.join(texto[:].split("."))
    texto2 = ' '.join(texto1[:].split(","))
    texto3 = ' '.join(texto2[:].split(":"))
    texto4 = ' '.join(texto3[:].split(";"))
    texto5 = ' '.join(texto4[:].split("-"))
    texto6 = ' '.join(texto5[:].split("!"))
    texto7 = ' '.join(texto6[:].split("?"))
    return texto7
def inverte(texto):
    inverte1= retira_pontuacao(texto).split()
    return inverte1[::-1]