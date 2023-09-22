def inverte(frase):
    """ Recebe uma frase e retorna outra que contenha as mesmas palavras porém, na ordem inversa e sem letras maiusculas e sem pontuaçao;
    string->string """
    if ";" in frase:
        frase=frase.replace(";"," ")
    if "-" in frase:
         frase=frase.replace("-"," ")
    if "," in frase:
        frase=frase.replace(","," ")
    if ":" in frase:
        frase=frase.replace(":"," ")
    if "." in frase:
        frase=frase.replace("."," ")
    if "!" in frase:
        frase=frase.replace("!"," ")
    if "?" in frase:
        frase=frase.replace("?"," ")
    x=frase.split()
    y=' '.join(x[::-1])
    return y.lower()