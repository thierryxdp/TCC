def retira_pontuacao(frase):
    """Essa função recebe uma frase com caracteres de pontuação e 
    retorna essa frase com todos os caracteres substituidos por
    espaço. str->str"""
    x = str.replace(frase,".",' ')
    y = str.replace(x,",",' ')
    z = str.replace(y,":",' ')
    h = str.replace(z,";",' ')
    d = str.replace(h,"-",' ')
    e = str.replace(d,"!",' ')
    i = str.replace(e,"?",' ')
    return i