"Função que conta o número de frases dado a entrada-texto"
def conta_frases(texto):
    str.replace(texto,"!","")
    str.replace(texto,".","")
    str.replace(texto,"?","")
    str.replace(texto,"...","")
    return (len(texto.split()))