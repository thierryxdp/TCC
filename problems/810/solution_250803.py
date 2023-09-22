def retira_pontuacao(frase):
    frase=str.replace(frase,"-"," ")
    frase=str.replace(frase,", "," ")
    frase=str.replace(frase,": "," ")
    frase=str.replace(frase,"; "," ")
    frase=str.replace(frase,". "," ")
    frase=str.replace(frase,"! "," ")
    frase=str.replace(frase,"? "," ")
    return frase
def inverte(a):
    b=()
    a=str.lower(a)
    a=retira_pontuacao(a)
    a=str.split(a," ")
    b=a[0:]
    
    return b