def retira_pontuacao(frase):
    """Função que dado uma frase, retirará todas os caracteres de pontuação da mesma"""
    frase.split(" ")
    if '.' in frase:
        return frase.replace('.', ' ')
    if '?' in frase:
        return frase.replace('?', ' ')