def uppCons(string):
    novafrase= " "
    i= 0
    
    while i < len(string):
        if string[i] in "aeiouAEIOU":
            novafrase = novafrase + string[i].upper()
        if string[i] not in "aeiouAEIOU":
            novafrase= novafrase + string[i].lower()
        i=i+1
    return novafrase