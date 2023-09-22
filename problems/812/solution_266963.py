def retira_pontuacao(frase):
    """Retorna a frase de entreda em que todos os caracteres de pontuação são substituidos por espaço. string -> string"""
    (str.replace(frase,"!"," "))
    (str.replace(frase,"."," "))
    (str.replace(frase,"?"," "))
    (str.replace(frase,","," "))
    (str.replace(frase,";"," "))
    (str.replace(frase,"-"," "))
    return frase