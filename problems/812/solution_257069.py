def retira_pontuação(frase):
    """função que dada uma frase retorna onde todos os caracteres de pontução tenham
    sido substituídos por espaço 
    str --> str """
    texto = ".".join(frase)
    texto = ",".join(frase)
    texto = ":".join(frase)
    texto = ";".join(frase)
    return texto