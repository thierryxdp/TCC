def retira_pontuaçao(frase):
    frase=str.replace(frase,"," , " ")
    frase=str.replace(frase,"!" , " ")
    frase=str.replace(frase,"?" , " ")
    frase=str.replace(frase,":" , " ")
    frase=str.replace(frase,";" , " ")
    frase=str.replace(frase,"." , " ")
    frase=frase.lower()
    invertida = ' '.join(palavra[::-1] for palavra in frase.split())
    frase=list(str.split(frase," "))
    frase=str.join(" ",frase([::-1]))      
    return frase