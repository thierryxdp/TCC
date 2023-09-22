def inverte(frase):
    """Cálculo de uma função que dada uma frase retorne outra frase que contenha as mesmas palavras da frase de entrada na ordem inversa 
       e sem pontuação e sem letras maiusculas.
    
       Parameters:
       frase: corresponde a frase que será mudada
       
       Returns:
       Retorna a nova frase contendo as mesmas palavras da frase de entrada, e na ordem inversa,
       e sem letras maiusculas e sem pontuação dado que:
       str -> str
    """
    x = str.lower(frase)
    if str.count(x,",") > 0:
        x=str.replace(x, ",", "")
    if str.count(x,";") > 0:
        x=str.replace(x, ";", " ")
    if str.count(x,":") > 0:
        x=str.replace(x, ":", " ")
    if str.count(x,"_") > 0:
        x=str.replace(x, "_", " ")
    if str.count(x,"-") > 0:
        x=str.replace(x, "-", " ")
    if str.count(x,".") > 0:
        x=str.replace(x, ".", "")
    if str.count(x,"!") > 0:
        x=str.replace(x, "!", "")
    if str.count(x,"?") > 0:
        x=str.replace(x, "?", "")
    return str.join(" ", str.split(x," ")[::-1]