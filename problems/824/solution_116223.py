def uppCons(frase:str) -> str:
    i=0
    a=''
    while i<len(frase):
        if frase [i] in 'bcdfghjklmnpqrstvwxyzç':
            a += frase[i].upper()
        else:
            a += frase[i]
        i+=1
    return a