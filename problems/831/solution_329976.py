def lingua_p(palavra):
    """Funcao que recebe uma palavra e retorna ela traduzida da a lingua do P. str=>str"""
    palavradop=' '
    for letra in range (len(palavra)):
        if palavra [letra] in "aeiouáéíóúêôûâîãõ":
            palavradop= palavradop+palavra[letra]+'p'+palavra[letra]
        else:
            palavradop= palavradop+palavra[letra]
    return palavradop