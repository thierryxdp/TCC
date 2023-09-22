def inverte(frase):
    frase=str.split(frase,",")
    frase1=str.join(" ",frase)
    frase2=str.split(frase1,".")
    frase3=str.join(" ",frase2)
    frase4=str.split(frase3,"!")
    frase5=str.join(" ",frase4)
    return str.lower(frase3[::-1])