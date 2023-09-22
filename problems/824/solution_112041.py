def uppCons(string):
    novafrase= " "
    i= 0
    string[i] = letra
    while i < len(string):
        if string[i] != "aeiouAEIOU":
            novafrase = novafrase + string.upper(letra)
        if string[i] == "aeiouAEIOU":
            novafrase= novafrase + string[i]
        i=i+1
    return novafrase