def inverte(x):
    """dada uma frase, retorna uma outra frase que contenha as mesmas palavras da frase de entrada na ordem inversa, sem letras maiúsculas e sem pontuação   (str --> str)"""
    k = str.lower(x)
    k = str.replace(k,".","")
    k = str.replace(k,"!","")
    k = str.replace(k,"?","")
    k = str.replace(k,"-"," ")
    k = str.replace(k,",","")
    k = str.split(k," ")
    k = k[::-1]