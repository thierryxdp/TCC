def inverte(frase):
    "função que recebe uma frase(str) e retorna uma frase com as letras minúsculas, ordem de palavras trocadas e sem pontuação"
   
    frase0 =  str.replace(frase,"...",".")
    frase1 =  str.replace(frase0,","," ")
    frase2 =  str.replace(frase1,":"," ")
    frase3 =  str.replace(frase2,";"," ")
    frase4 =  str.replace(frase3,"."," ")
    frase5 =  str.replace(frase4,"!"," ")
    frase6 =  str.replace(frase5,"?"," ")
    frase7 =  str.replace(frase6,"."," ")
    frase8 =  str.replace(frase7,"-"," ")
    minuscula = str.lower(frase8)
    frase9 = str.split(minuscula," ")
    frase10 = list.reverse(frase9)
    frase11 = str.join(" ",frase10)
    return frase11