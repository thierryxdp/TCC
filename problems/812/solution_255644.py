def retira_pontuacao(frase):
    """Retorna a frase dada sem pontuação
       Entrada: str
       Saida: str
    """
    x = frase.split()
    if '.' in x:
        list.remove(x, .)
    return x