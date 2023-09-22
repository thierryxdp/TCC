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

def quant_palavras(frase):
    """Funcao retorna quantas palavras existem em uma frase dada
    na forma de string: frase """

    retira_pontuacao(frase)
    
    p = frase.split(" ")

    p = list(filter(lambda x: x != "", p))
    
    return len(p)