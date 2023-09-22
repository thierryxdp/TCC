def inverte(frase):
    """Funcao que dada uma frase, inverte suas palavras, remove a pontuação e retira as letras maiúsculas, retornando uma
    nova frase
    str -> str"""
    SemPontuacao = retira_pontuacao(frase)
    Minusculas = str.lower(SemPontuacao)
    Separa = str.split(Minusculas)
    Inverte = Separa[::-1]
    Junta = str.join(' ', Inverte)
    return Junta