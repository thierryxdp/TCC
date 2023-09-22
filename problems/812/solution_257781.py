def retira_pontuacao(frase):
    """Essa função recebe uma frase com caracteres de pontuação e 
    retorna essa frase com todos os caracteres substituidos por
    espaço. str->str"""
    if "," in frase:
        frase = str.replace(frase,",",' ')
        return frase
    elif "!" in frase:
        frase = str.replace(frase,"!",' ')
        return frase
    elif "?" in frase:
        frase = str.replace(frase,"?",' ')
        return frase
    elif "." in frase:
        frase = str.replace(frase,".",' ')
        return frase
    elif "-" in frase:
        frase = str.replace(frase,"-",' ')
        return frase