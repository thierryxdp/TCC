def retira_pontuacao(frase):
    """essa funçao recebe uma frase e a retorna com sinais de pontuaçao substituidos por espaço"""
    """entrada: str"""
    """saida: str"""
    for "." in string.punctuation:
        frase = str.replace(frase,"."," ")
    for "?" in string.punctuation:
        frase = str.replace(frase,"?"," ")
    for "!" in string.punctuation:
        frase = str.replace(frase,"!"," ")
    for "," in string.punctuation:
        frase = str.replace(frase,",", "")
    for "-" in string.punctuation:
        frase = str.replace(frase,"-", "")
    for "..." in string.punctuation:
        frase = str.replace(frase,"..."," ")
    for ":" in string.punctuation:
        frase = str.replace(frase,":"," ")
    for ";" in string.punctuation:
        frase = str.replace(frase,";"," ")
        return frase