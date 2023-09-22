def conta_frases(x: str) -> int:
    """Dado um texto, retorna o número de frases que o texto possui

       Parameters:
       x: String que representa o texto a ser contado

       Return:
       O número de frases que um texto possui, dado o parâmetro "x", e sabendo
       que cada frase é terminada por um ponto final, um ponto de exclamação,
       um ponto de interrogação ou três pontos em sequència (reticências)

       Examples:
       conta_frases("Preciso tirar um cochilo. Meus Deus! Que horas são?
       Vou perder a minha aula...") == 4
       conta_frases("Oi. Como! Você... está?") == 4
       conta_frases("Oi.") == 1
    """

    y = str.replace(x, "...", "@")

    a = str.count(y, ".")
    b = str.count(y, "!")
    c = str.count(y, "?")
    d = str.count(y, "@")

    return a + b + c + d