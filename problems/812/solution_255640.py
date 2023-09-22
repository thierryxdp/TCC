def retira_pontuacao(frase):
    """Retorna a frase dada sem pontuação
       Entrada: str
       Saida: str
    """
    lista = frase.split()
    x = list.remove(lista, .)
    return x