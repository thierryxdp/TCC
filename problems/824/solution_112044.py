def uppCons(string):
    novafrase= " "
    i= 0
    letra =string[i]
    while i < len(string):
        if string[i] != "aeiouAEIOU":
            novafrase = novafrase + letra.upper()
        if string[i] == "aeiouAEIOU":
            novafrase= novafrase + string[i]
        i=i+1
    return novafrase