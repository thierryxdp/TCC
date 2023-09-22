def inverte(frase):
    frase=str.replace(frase,"!"," ")
    frase=str.replace(frase,"..."," ")
    frase=str.replace(frase,"."," ")
    frase=str.replace(frase,"?"," ")
    frase=str.replace(frase,";"," ")
    frase=str.replace(frase,":"," ")
    frase=str.replace(frase,","," ")
    frase=str.replace(frase,"-"," ")
    listaPalavras= str.split(frase, )
    invertida= listaPalavras[::-1]
    invertida= str.join(" ",invertida)
    invertida= str.lower(invertida)
    return invertida