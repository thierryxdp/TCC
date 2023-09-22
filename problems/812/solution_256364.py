def retira_pontuacao(frase):
    """Funçao que recebe uma frase e substitui todas as pontuacoes 
       por espaco."""
    pontuacao = ['!', '?', '#', '$', '@', '%', '&', '*', ',', '.', '-']
    for trocar in pontuacao:
        frase = frase.replace(trocar,' ')
    return frase