def retira_pontuaçao(frase):
    frase=str.replace(frase,"," , " ")
    frase=str.replace(frase,"!" , " ")
    frase=str.replace(frase,"?" , " ")
    frase=str.replace(frase,":" , " ")
    frase=str.replace(frase,";" , " ")
    frase=str.replace(frase,"." , " ")
    frase=frase.lower(frase)
    print( {}'.format(frase))
    invertida = ' '.join(palavra[::-1] for palavra in frase.split())
    print( {}'.format(invertida))
    return frase

def inverte(frase):
          frase=list(str.split(frase," "))
          frase=str.join(" ",frase([::-1]))
          return frase