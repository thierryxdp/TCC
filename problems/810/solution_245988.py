def inverte(Frase):
    """Função que inverte as palavras de uma 
    frase, retirando pontuação e sem letras maiúsculas
    Parâmetros de Entrada: Str
    Valor de Saída: Str"""
    Frase = retira_pontuacao(Frase)
    Frase = Frase.lower()
    frase_final = Frase.split(" ")
    fraseF = frase_final[::-1]
    return " ".join(fraseF).lstrip()