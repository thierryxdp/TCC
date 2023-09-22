def retira_pontuação(frase):
    """função que dada uma frase retorna onde todos os caracteres de pontução tenham
    sido substituídos por espaço 
    str --> str """
    x = "-", "," , ":" , ";", "."
    y = "       "
    uni= frase.maketrans(x,y)
    return (frase.translate(uni))