def conta_frases (frase):
    novafrase =  str.replace( frase, ";", " ")
    novafrase1 = str.replace(novafrase, "." , " " )
    novafrase2 = str.replace(novafrase1,  ":", " ")
    novafrase3 = str.replace(novafrase2, " ?" , " ")
    novafrase4 = str.replace(novafrase3, "," , " ")
    novafrase5 = str.replace(novafrase4, "!", " ")
    novafrase6 = str.replace(novafrase5, "-", " ")
    return novafrase6