def uppCons(string):
    novafrase= ""
    i= 0
    
    while i < len(string):
        if string[i] not in  "aeiouAEIOUÃÁÀáàâéÈÉÍÌÓÚ":
            novafrase = novafrase + string[i].upper()
        if string[i]  in "aeiouAEIOUÃÁÀáàâéÈÉÍÌÓÚ":
            novafrase= novafrase + string[i]
        i=i+1
    return novafrase