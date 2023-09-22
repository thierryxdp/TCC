if "-" in frase:
        frase = str.replace(frase,"-"," ")
    if "," in frase:
        frase = str.replace(frase,","," ")
    if ":" in frase:
        frase = str.replace(frase,":"," ")
    if "." in frase:
        frase = str.replace(frase,"."," ")
    if ";" in frase:
        frase = str.replace(frase,";"," ")
    if "?" in frase:
        frase = str.replace(frase,"?"," ")
    if "!" in frase:
        frase = str.replace(frase,"!"," ")
    
    lista_frase = frase.split(" ")
    posicao = len(lista_frase) + 1
    inverter = lista_frase[posicao:-(posicao): -1]
    concatenar = str.join(" ",inverter)
    
    return str.lower(concatenar)