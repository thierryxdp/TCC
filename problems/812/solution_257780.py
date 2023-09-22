def retira_pontuacao(frase):
    """Essa função recebe uma frase com caracteres de pontuação e 
    retorna essa frase com todos os caracteres substituidos por
    espaço. str->str"""
    frase = str.replace(frase,",",' ')
    return frase