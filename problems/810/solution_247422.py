def inverte(frase):
    """A função retorna uma outra frase que contenha as mesmas palavras
    da frase de entrada na ordem inversa, sem maiúscula, e sem a
    pontuação.
    str-->str."""
    if "-" in frase:
        frase = str.replace(frase,"-"," ")
    if "," in frase:
        frase = str.replace(frase,",","")
    if ":" in frase:
        frase = str.replace(frase,":","")
    if "." in frase:
        frase = str.replace(frase,".","")
    if ";" in frase:
        frase = str.replace(frase,";","")
    if "?" in frase:
        frase = str.replace(frase,"?","")
    if "!" in frase:
        frase = str.replace(frase,"!","")
    
    nova_lista = str.split(frase,"")
    posicao = len(nova_lista) + 1
    mudanca = [posicao:-(posicao): -1]
    concatenar = str.join("",mudanca)
    return str.lower(concatenar)