def inverte(frase):
    frase1=str.replace(frase,'!'," ")
    frase2=str.replace(frase1,'.'," ")
    frase3=str.replace(frase2,'-'," ")
    frase4=str.replace(frase3,':'," ")
    frase5=str.replace(frase4,','," ")
    frase6=str.replace(frase5,';'," ")
    frase7=str.replace(frase6,'?'," ")
    cortada=str.split(frase7)
    invertida=cortada[::-1]
    frasefinal=str.join(" ",invertida)
    return frasefinal