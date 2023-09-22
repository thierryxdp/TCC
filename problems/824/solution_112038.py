def uppCons(string):
    novafrase= " "
    i= 0
    while i < len(string):
        if string[i] != "aeiouAEIOU":
        novafrase = novafrase + upper(string[i])
        if string[i] == "aeiouAEIOU":
        novafrase= novafrase + string[i]
        i=i+1
    return novafrase