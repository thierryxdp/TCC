def retira_pontuacao(f):
    """Funcao retorna a frase dada na forma de string: f com os seus
    caracteres de pontuacao substituidos por espaco """
    
    f = f.split("...")

    f = str.join("", f)

    f = f.split(".")

    f = str.join("", f)

    f = f.split(",")

    f = str.join("", f)

    f = f.split("?")

    f = str.join("", f)

    f = f.split("!")

    f = str.join("", f)

    f = f.split("-")

    f = str.join("", f)

    f = f.split(":")

    f = str.join("", f)

    return f