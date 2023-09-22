def retira_pontuacao(frase):
    """Função que, dada uma frase, retorna a frase sem pontuação.
    str-> str"""
  
    frase.split(".") + ' '.join(frase.split("."))
    frase.split("!") + ' '.join(frase.split("!"))
    frase.split("?") + ' '.join(frase.split("?"))
    frase.split(",") + ' '.join(frase.split(","))
    frase.split("...") + ' '.join(frase.split("..."))
    frase.split("-") + ' '.join(frase.split("-"))
    return frase.split(" ")