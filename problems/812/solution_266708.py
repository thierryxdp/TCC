def retira_pontuacao(frase):
    """Função que recebe uma frase e substitui todas as pontuações por espaço. str -> str"""
    especias = ['!', '?', '#', '$', '@', '%', '&', '*', ',', '.', '-']
    for trocar in especias:
        frase = frase.replace(trocar,' ')
    return frase