def retira_pontuacao(frase):
    """recebe uma string com uma frase e retorna uma string com a mesma frase
    com seus caracteres de pontuação substituidos por espaço"""

    frase1 = frase.replace("-", " ")
    frase2 = frase1.replace(",", " ")
    frase3 = frase2.replace(":", " ")
    frase4 = frase3.replace(";", " ")
    frase5 = frase4.replace(".", " ")
    frase6 = frase5.replace("!", " ")
    frase7 = frase6.replace("?", " ")
    
    return frase7