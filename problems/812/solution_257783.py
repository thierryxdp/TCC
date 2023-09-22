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
    elif "," and "." in frase:
        frase1 = str.replace(frase,",",' ')
        frase2 = str.replace(frase1,".",' ')
        return frase2
    elif "-" and "." in frase:
        frase1 = str.replace(frase,"-",' ')
        frase2 = str.replace(frase1,".",' ')
        return frase2
    elif "," and "?" in frase:
        frase1 = str.replace(frase,",",' ')
        frase2 = str.replace(frase1,"?",' ')
        return frase2
    elif "-" and "!" in frase:
        frase1 = str.replace(frase,"-",' ')
        frase2 = str.replace(frase1,"!",' ')
        return frase2