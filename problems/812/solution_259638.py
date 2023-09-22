def retira_pontuacao(frase):
    """Função que, dada uma frase, retorna a frase sem pontuação.
    str-> str"""
    f1=frase.split(".")
    f2=' 'join(f1.split("."))
    f3=f2.split(",")
    f4=' 'join(f2.split(","))
    f5=f4.split("!")
    f6=' 'join(f4.split("!"))
    f7=f6.split("?")
    f8=' 'join(f6.split("?"))
    f9=f8.split("...")
    f10=' 'join(f8.split("..."))
    return f10[::-1]