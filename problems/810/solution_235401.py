def inverte (frase):
    """Funcao que, dado uma frase, retorna ela na ordem inversa, sem letras maiúsculas e sem a pontuação
    str-->str"""
    frase= str.lower(str.join(" ", (str.split(retira_pontuacao(frase))[::-1])))
    return frase