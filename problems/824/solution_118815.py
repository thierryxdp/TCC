def uppCons(frase):
    "str->str"
    i=0
    z=0
    consoantes=""
    vogais=""
    while i<len(frase):
        if frase[0] in "bcdfghjklmnpqrstvwyz":
            consoantes=consoantes+frase[i]
        i=i+1
    while z<len(frase):
        if frase[0] in "aeiouAEIOU":
            vogais=vogais+frase[z]
        z=z+1
    return str.join(consoantes,vogais)