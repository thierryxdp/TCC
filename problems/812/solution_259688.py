def retira_pontuacao(frase):
    """Função que, dada uma frase, retorna a frase sem pontuação.
    str-> str"""
    frase = ()
    f1 = frase.split(".") + ' '.join(frase.split("."))
    f2 = f1.split("!") + ' '.join(f1.split("!"))
    f3 = f2.split("?") + ' '.join(f2.split("?"))
    f4 = f3.split(",") + ' '.join(f3.split(","))
    f5 = f4.split("...") + ' '.join(f4.split("..."))
    f6=f5.split("-") + ' '.join(f5.split("-"))
    return f6.split(" ")