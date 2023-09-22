def uppCons(frase):
    i = 0
    nova_frase = ''
    while i < len(frase):
        if frase[i] not in "AEIOUaeiouãáàâóíé":
            nova_frase += str.upper(frase[i])
        else:
            nova_frase += frase[i]
        i+=1
    return nova_frase