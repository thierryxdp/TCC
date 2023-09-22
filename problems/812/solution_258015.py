def retira_pontuacao(frase):
    """Essa função recebe uma frase com caracteres de pontuação e 
    retorna essa frase com todos os caracteres substituidos por
    espaço. str->str"""
    x = str.replace(frase,".",' ')
    y = str.replace(frase,",",' ')
    z = str.replace(frase,":",' ')
    h = str.replace(frase,";",' ')
    d = str.replace(frase,"-",' ')
    return d