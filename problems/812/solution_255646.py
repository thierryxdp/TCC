def retira_pontuacao(frase):
    """Retorna a frase dada sem pontuação
       Entrada: str
       Saida: str
    """
    if '.' in frase:
        list.remove(frase, '.')
    return frase