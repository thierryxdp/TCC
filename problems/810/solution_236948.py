def retira_pontuacao(frase):
    frase=str.replace(frase,"," , " ")
    frase=str.replace(frase,"!" , " ")
    frase=str.replace(frase,"?" , " ")
    frase=str.replace(frase,":" , " ")
    frase=str.replace(frase,";" , " ")
    frase=str.replace(frase,"." , " ")
    frase=frase.lower()
    frase=frase.split()
    frase=str.join(" ",frase([::-1])
    return frase