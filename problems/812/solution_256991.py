def retira_pontuacao(string):
    """
    str->str
    :param string: Recebe uma frase
    :return: Retira os caracteres especiais de pontuação da frase 
    """
    for char in ".!?-:;,":
            string = string.replace(char, " ")
    return string