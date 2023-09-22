def retira_pontuacao(frase):
    """Retorna a frase dada sem pontuação
       Entrada: str
       Saida: str
    """
    x = frase.split()
    return list.remove(x, ".")