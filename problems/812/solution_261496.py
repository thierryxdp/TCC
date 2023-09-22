def retira_pontuacao(frase):
    """Funcao que substitui os caracteres de pontuacao por espaco
    entrada: string
    saida: string"""
    if ":" in frase:
        return str.replace(frase,":"," ")
    elif "-" in frase:
        return str.replace(frase,"-"," ")
    if ";" in frase:
        return str.replace(frase,";"," ")
    elif "." in frase:
        return str.replace(frase,"."," ")
    if "!" in frase:
        return str.replace(frase,"!"," ")
    elif "?" in frase:
        return str.replace(frase,"?"," ")
    if ", " in frase:
        return str.replace(frase,","," ")