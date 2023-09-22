def retira_pontuacao(frase):
    """Função retira as pontuações e substitui por espaço de frase inserida pelo usuario e retorna
       Parametro: str -> str"""
    po = ['!','?',',','.',':',';','/']
    tos = ['?','.']
    for substituir in po and for substituir in tos:
        frase = frase.replace(substituir,' ')
        return frase