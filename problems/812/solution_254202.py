def retira_pontuação(frase):
    if frase[len(frase)] == ".":
        return str.replace(frase,".", "")
 
    if frase[len(frase)] == "!":
        return str.replace(frase,"!","")