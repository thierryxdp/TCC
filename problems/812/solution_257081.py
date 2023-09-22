def retira_pontuacao(frase):
    """Função retira as pontuações e substitui por espaço de frase inserida pelo usuario e retorna
       Parametro: str -> str"""
    pontos = ['!','?',',','.',':',';','/']
    for substituir in pontos:
        frase = frase.replace(substituir,' ')
        return frase