def inverte(frase):
    """ Função que recebe uma frase as inverte e retorna uma outra frase
        str->str"""
    frase = srt.replace(frase,"!", " ")
    frase = srt.replace(frase,"?", " ")
    frase = srt.replace(frase,".", " ")
    frase = srt.replace(frase,",", " ")
    frase = srt.replace(frase,"-", " ")
    frase = srt.replace(frase,":", " ")
    frase = srt.replace(frase,";", " ")
    return frase
a1 = str.split(frase, " ")
a1 = a1[::-1]
a2 = str.join(" ",a1)
a3 = str.lower(a2)