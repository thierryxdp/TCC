def retira_pontuacao(frase):
    """Funcao que dada uma frase, retira toda a pontuacao."""
    nova_frase = frase[:]
    for pnt in [".", ",", "-", "!", "?", ";", ":"]:
        nova_frase = str.replace(nova_frase, pnt, " ")
    return nova_frase