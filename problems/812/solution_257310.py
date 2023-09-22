def retira_pontuacao(x: str) -> str:
    """Recebe um texto e retorna o mesmo texto, mas sem a pontuação

       Parameters:
       x: String a ser modificada

       Return:
       Um texto no qual todo caractere de pontuação (travessão, vírgula,
       dois pontos, ponto e vírgula, ponto final, ponto de exclamação e
       ponto de interrogação) é substituído por espaço, dado o parâmetro "x"

       Examples:
    """

    a = str.replace(x, "-", " ")
    b = str.replace(a, ",", " ")
    c = str.replace(b, ":", " ")
    d = str.replace(c, ";", " ")
    e = str.replace(d, ".", " ")
    f = str.replace(e, "!", " ")
    g = str.replace(f, "?", " ")

    return g