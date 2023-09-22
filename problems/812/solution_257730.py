def retira_pontucao(frase):
    """funcaocalcula e retorna espacso em branco no lugar de caracteres de pontiacao"""
    if "-" in frase:
        return str.replace(frase,"-"," ")
    if "," in frase:
        return str.replace(frase,","," ")
    if ":" in frase:
        return str.replace(frase,":"," ")
    if ";" in frase:
        return str.replace(frase,":"," ")