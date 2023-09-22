def uppCons(frase):
  
    frase1 = list(frase)
    for i in range(len(frase1)):
        if frase1[i] not in "aeiouãúé":
            frase1[i] = frase1[i].upper()
    frase1 = "".join(frase1)
    return frase1