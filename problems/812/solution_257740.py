def retira_pontuacao(frase):
    """funcaocalcula e retorna espacso em branco no lugar de caracteres de pontiacao
    string,string-->string"""
    if "-":
        frase=str.replace(frase,"-"," ")
    if ",":
        frase=str.replace(frase,","," ")
    if ":":
        frase=str.replace(frase,":"," ")
    if ";":
        frase=str.replace(frase,":"," ")
    if "!":
        frase=str.replace(frase,"!"," ")
        return frase