def retira_pontuacao(f):
    """Funcao retorna a frase dada na forma de string: f com os seus
    caracteres de pontuacao substituidos por espaco """
    
    f = f.split("...")

    f = str.join(" ", f)

    f = f.split(".")

    f = str.join(" ", f)

    f = f.split(",")

    f = str.join(" ", f)

    f = f.split("?")

    f = str.join(" ", f)

    f = f.split("!")

    f = str.join(" ", f)

    f = f.split("-")

    f = str.join(" ", f)

    f = f.split(":")

    f = str.join(" ", f)

    return f

def inverte(f):
    """Funcao retorna a frase dada na forma de string: f com os seus caracteres
    de pontuacao substituidos por espaco, as letras maiusculas substituidas por
    minusculas e com as palavras da frase na ordem inversa """

    f = str.lower(f)
	
    f = retira_pontuacao(f)
    
    f = f.split(" ")

    f = list(filter(lambda x: x != " ", f))
    
    f1 = f[::-1]
    
    f1 = str.join(" ", f1)

    return f,f1