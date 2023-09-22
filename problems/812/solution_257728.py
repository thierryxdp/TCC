def retira_pontucao(frase):
    """funcaocalcula e retorna espacso em branco no lugar de caracteres de pontiacao"""
    if "-":
        return str.replace(frase,"-"," ")
    if ",":
        return str.replace(frase,","," ")
    if ":":
        return str.replace(frase,":"," ")
    if ";":
        return str.replace(frase,":"," ")