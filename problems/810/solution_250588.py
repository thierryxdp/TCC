def retira_ponruacao(frase):
    d=[".",",","-",":",";"]
    for c in d:
        frase=str.replace(frase,c," ")
    return frase

def inverte(frase):
    f=list(frase)
    return list.sort(x,reverse=True)