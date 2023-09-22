def inverte (frase):
    if "-" in frase:
        frase=str.replace(frase,"-"," ")
    if "," in frase:
        frase=str.replace(frase,","," ")
    if ":" in frase:
        frase=str.replace(frase,":"," ")
    if ";" in frase:
        frase=str.replace(frase,";"," ")
    if "." in frase:
        frase=str.replace(frase,"."," ")
    if "?" in frase:
        frase=str.replace(frase,"?"," ")
    if "!" in frase:
        frase=str.replace(frase,"!"," ")
    if "_" in frase:
        frase=str.replace(frase,"-"," ")
    n=str.lower(frase)
    n1=n.split(" ")
    n2=n1[::-1]
    n3=str.join(" ",n2)
    n4=str.strip(n3," ")
    return str.replace(n4," "," ")