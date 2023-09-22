def retira_pontuacao(String):
    '''Função que retira caracteres de pontuação de uma frase'''
    '''str -> str'''
    return str.replace(String, "!-?.;,", "")