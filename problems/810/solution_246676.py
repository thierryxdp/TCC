def inverte(frase):
    """Retorna ,dada uma frase, uma outra frase que contenha
       as mesmas palavras da frase de entrada na ordem
       inversa, sem letras maiúsculas, e sem a pontuação.
       str -> str"""
    frase = str.lower(frase)
    frase = str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase,"-",""),"...",""),", ",""),":",""),";",""),"!",""),"?",""),".","")
    frase = str.split(frase," ")
    frase = str.reverse(frase)
    return frase