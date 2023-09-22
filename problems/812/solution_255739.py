def retira_pontuacao(frase):
    """ESSA FUNÇÃO DADA UMA FRASE RETORNA A MESMA FRASE ONDE TODOS OS CARACTERES, SÃO SUBSTITUIDOS POR UM ESPAÇO"""
    frase = str.split(frase, ".")
    frase = str.join(" ",frase)
    return frase