def retira_pontuacao(frase, c):
    """ESSA FUNÇÃO DADA UMA FRASE RETORNA A MESMA FRASE ONDE TODOS OS CARACTERES, SÃO SUBSTITUIDOS POR UM ESPAÇO"""
    c = "!",["."],[","],[":"],["-"]
    frase = str.split(frase, c)
    frase = str.join(" ",frase)
    return frase