def conta_frases(frases):
    frase1=str.join("/",str.split(frases,"?"))
    frase2=str.join("/",str.split(frase1,"!"))
    frase3=str.join("/",str.split(frase2,"..."))
    frase4=str.join("/",str.split(frase3,"."))
    nfrases=len(str.split(frase4,"/"))-1
    return nfrases