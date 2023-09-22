def retira_pontuaçao(frase):
    frase=str.replace(frase,"," , " ")
    frase=str.replace(frase,"!" , " ")
    frase=str.replace(frase,"?" , " ")
    frase=str.replace(frase,":" , " ")
    frase=str.replace(frase,";" , " ")
    frase=str.replace(frase,"." , " ")
    frase=frase.lower(frase)
    frase = input('Digite uma frase: ')
    print( {}'.format(frase))
    invertida = ' '.join(palavra[::-1] for palavra in frase.split())
    print( {}'.format(invertida))
    return frase

def inverte(frase):
          frase=list(str.split(frase," "))
          frase=str.join(" ",frase)
          frase= frase[::-1]
          return frase