def uppCons(frase):
    consoantes = ["b","c","d","f","g","h","j","k","l","m","n","p",
                  "q","r","s","t","v","w","x","y","z"]
    lista1= list(frase)
    for i,c in enumerate(lista1):
        if c in consoantes:
            lista1[i] = c.upper()
    return ("".join(lista1))