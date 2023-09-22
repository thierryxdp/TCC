def inverte(frase):
    frase=str.split(frase,",")
    frase1=str.join(" ",frase)
    frase2=str.split(frase1,".")
    frase3=str,join(" ",frase2)
    return str.lower(frase3[::-1]