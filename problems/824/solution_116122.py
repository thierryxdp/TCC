def uppCons(frase):
    letra=0
    frasenova=[]
    vocais=['a','e','i','o','u']
    while letra<len(frase):
        if frase[letra] not in vocais:
            frasenova.append(str.lower(frase[letra]))
            letra+=1
        else:
            frasenova.append(frase[letra])
            letra+=1
    return ''.join(frasenova)