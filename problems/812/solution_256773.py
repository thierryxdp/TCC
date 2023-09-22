def retira_pontuaçao(frase):
    frase=str.replace(frase,"," , " ")
    frase=str.replace(frase,"!" , " ")
    frase=str.replace(frase,"?" , " ")
    frase=str.replace(frase,":" , " ")
    frase=str.replace(frase,";" , " ")
    frase=str.replace(frase,"." , " ")
    return frase