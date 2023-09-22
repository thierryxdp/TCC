def retira_pontuacao(frase):
    """Função que recebe uma frase e retorna uma frase onde todos os
    caracteres de pontuação tenham sido substituídos por espaços.
    str->str
    """
    frase = str.replace(frase, "-", " " )
    frase = str.replace(frase, ",", " " )
    frase = str.replace(frase, ":", " " )
    frase = str.replace(frase, ";", " " )
    frase = str.replace(frase, "?", " " )
    frase = str.replace(frase, "!", " " )
    frase = str.replace(frase, ".", " " )
    frase = str.replace(frase, "...", " " )
    return frase